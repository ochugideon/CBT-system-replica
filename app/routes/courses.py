import io
import pandas as pd
import json

from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.models.courses import Courses
from app.schemas.courses import CoursesBase

router = APIRouter(
  prefix='/api/courses',
  tags=['Course']
)

@router.post('/admin/add-courses', status_code=status.HTTP_201_CREATED)
async def add(file: UploadFile, db: Session = Depends(get_db)):
  if not file.filename.endswith('.csv'):
    raise HTTPException(
      status_code=status.HTTP_400_BAD_REQUEST,
      detail='Invalid file format. Only CSV files are allowed.'
    )
  contents = await file.read()
  buffer = io.StringIO(contents.decode('utf-8'))
  reader = pd.read_csv(buffer)
  
  expected_headers = ['course_id', 'course_code', 'course_title']
  if not reader.columns.tolist() == expected_headers:
    raise HTTPException(
        status_code=400,
        detail=f"CSV headers missing. File must contain: {', '.join(expected_headers)}"
    )
    
  existing_course_codes = set(
      res[0] for res in db.query(Courses.course_code).all()
  )
  
  courses = []
  already_exists = []

  for course in list(reader.to_dict(orient='records')):
    if course['course_code'] in existing_course_codes:
      already_exists.append(course)
    else:
      courses.append({
        "course_code": course['course_code'],
        "course_title": course['course_title']
      })
      
  db.bulk_insert_mappings(Courses, courses)
  db.commit()
  
  print(len(courses))
    
  return {
        "status": "success",
        "message": f"Successfully ingested {len(courses)} courses from admin batch.",
        "imported_count": len(courses),
        "skipped_count": len(already_exists),
        "skipped_courses": already_exists[:10]  # Show sample of skipped duplicates
    }


  # try:
  #   new_course = Courses(
  #       course_code = course.course_code.upper(),
  #       course_title = course.course_title.capitalize()
  #     )
      
  #   db.add(new_course)
  #   db.commit()
  #   db.refresh(new_course)
      
  #   return new_course
  
  # except IntegrityError:
  #   raise HTTPException(
  #     status_code=status.HTTP_409_CONFLICT,
  #     detail=f'course ({course.course_code.upper()}) already exists'
  #   )

@router.get('/', response_model=List[CoursesBase])
def aEll(db: Session = Depends(get_db)):
  exams =  db.query(Courses).all()
  return exams