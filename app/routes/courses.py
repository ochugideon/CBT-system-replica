from fastapi import APIRouter, Depends, status, HTTPException
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

@router.post('/new-course', status_code=status.HTTP_201_CREATED, response_model=CoursesBase)
def add(course: CoursesBase, db: Session = Depends(get_db)):
  try:
    new_course = Courses(
        course_code = course.course_code.upper(),
        course_title = course.course_title.capitalize()
      )
      
    db.add(new_course)
    db.commit()
    db.refresh(new_course)
      
    return new_course
  
  except IntegrityError:
    raise HTTPException(
      status_code=status.HTTP_409_CONFLICT,
      detail=f'course ({course.course_code.upper()}) already exists'
    )

@router.get('/', response_model=List[CoursesBase])
def aEll(db: Session = Depends(get_db)):
  exams =  db.query(Courses).all()
  return exams