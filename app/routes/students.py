import csv
import io
import urllib.parse

from datetime import datetime

from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.students import Students as StudentModel
from app.models.registered_students import Registered as RegisteredModel
from app.schemas.students import StudentBase, RegisteredStudentShow
from app.settings import hashing, random_code_gen

encrypt = hashing.Encrypt()
random_code = random_code_gen.create_access_code()
today = today = datetime.now().date().strftime('%d/%m/%Y')

print(today)

router = APIRouter(
  prefix='/api/students',
  tags=['Students']
)

@router.post("/admin/upload-students", status_code=status.HTTP_201_CREATED)
async def upload_admin_students(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    # 1. Validate file format
    if not file.filename.endswith(".csv"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file format. Only CSV files are allowed."
        )

    # 2. Read file content stream
    contents = await file.read()
    buffer = io.StringIO(contents.decode("utf-8"))
    reader = csv.DictReader(buffer)

    # 3. Validate headers
    expected_headers = {"student_id","full_name","reg_number","dept_id"}
    if not expected_headers.issubset(set(reader.fieldnames or [])):
        raise HTTPException(
            status_code=400,
            detail=f"CSV headers missing. File must contain: {', '.join(expected_headers)}"
        )

    # Fetch existing reg_numbers to prevent duplication/integrity errors
    existing_reg_numbers = set(
        res[0] for res in db.query(StudentModel.reg_number).all()
    )

    new_students = []
    skipped_records = []

    # 4. Parse and validate rows
    for row in reader:
        reg_num = row["reg_number"].strip()
        
        # Check if student is already in the system
        if reg_num in existing_reg_numbers:
            skipped_records.append(reg_num)
            continue

        try:
            student_obj = StudentModel(
                student_id=int(row["student_id"]),
                full_name=row["full_name"].strip(),
                reg_number=reg_num,
                dept_id=int(row["dept_id"])
            )
            new_students.append(student_obj)
            existing_reg_numbers.add(reg_num)
        except ValueError:
            raise HTTPException(
                status_code=422,
                detail=f"Data type error on row: {row}"
            )

    # 5. Bulk insert to DB
    if new_students:
        db.bulk_save_objects(new_students)
        db.commit()

    return {
        "status": "success",
        "message": f"Successfully ingested {len(new_students)} students from admin batch.",
        "imported_count": len(new_students),
        "skipped_count": len(skipped_records),
        "skipped_reg_numbers": skipped_records[:10]  # Show sample of skipped duplicates
    }
    

@router.get("/verify")
def verify_student_by_query(reg_number: str, db: Session = Depends(get_db)):
    # Sanitize white space and normalize case
    clean_reg_number = reg_number.strip().upper()
    
    student = db.query(StudentModel).filter(StudentModel.reg_number == clean_reg_number).first()
    if not student:
      raise HTTPException(status_code=404, detail="Student record not found.")
        
    return student
  
@router.post('/register-exam/{student_id}/{exam_id}', status_code=status.HTTP_201_CREATED, response_model=RegisteredStudentShow) 
def register_exam(exam_id: int,student: StudentBase,db: Session = Depends(get_db)):
    eligible_student = db.query(StudentModel).filter_by(reg_number=student.reg_number.upper()).first()
    
    if not eligible_student:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
            detail='no student with this record found.'
        )
    registered_student = db.query(RegisteredModel).filter_by(student_id= eligible_student.student_id, exam_id=exam_id).first()
    
    if registered_student:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail= 'student with this reg number already registered for this exam'
        )
    r_student = RegisteredModel(
        student_id = eligible_student.student_id,
        exam_id = exam_id,
        access_code_hash = encrypt.hash_string(random_code),
        registered_at = str(today)
    )
    db.add(r_student)
    db.commit()
    db.refresh(r_student)
    
    return r_student
 
@router.get('/')
def all_students(db: Session = Depends(get_db)):
  students = db.query(StudentModel).all()
  
  return students
  