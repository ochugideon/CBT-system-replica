import io
import pandas as pd

from fastapi import APIRouter, Depends, status, HTTPException, UploadFile
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.departments import Departments
from app.schemas.exams import ExamsBase, ExamsShow

router = APIRouter(
  prefix='/api/departments',
  tags=['Departments']
)

@router.post('/admin/add-departments', status_code=status.HTTP_201_CREATED)
def add(file: UploadFile, db: Session = Depends(get_db)):
  if not file.filename.endswith('.csv'):
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail='Invalid file format. Only CSV files are allowed.'
    )
    
  contents = file.file.read()
  buffer = io.StringIO(contents.decode('utf-8'))
  reader = pd.read_csv(buffer)
  
  expected_headers = ['dept_id', 'name', 'faculty']
  if not reader.columns.tolist() == expected_headers:
    raise HTTPException(
        status_code=400,
        detail=f"CSV headers missing. File must contain: {', '.join(expected_headers)}"
    )
  
  existing_depts_names = set(
      res[0] for res in db.query(Departments.name).all()
  )
  
  departments = []
  already_exists = []
  
  for dept in list(reader.to_dict(orient='records')):
    if dept['name'] in existing_depts_names:
      already_exists.append(dept)
    else:
      departments.append({
        "name": dept['name'],
        "faculty": dept['faculty']
      })
  
  db.bulk_insert_mappings(Departments, departments)
  db.commit()
  # db.refresh(new_exam)
  
  return {
        "status": "success",
        "message": f"Successfully ingested {len(departments)} departments from admin batch.",
        "skipped_records": already_exists[:10]
    }

@router.get('/', response_model=List[ExamsShow])
def aEll(db: Session = Depends(get_db)):
  departments =  db.query(Departments).all()
  return departments


