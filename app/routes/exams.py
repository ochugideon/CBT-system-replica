from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.exams import Exams
from app.schemas.exams import ExamsBase, ExamsShow

router = APIRouter(
  prefix='/api/exams',
  tags=['Exams']
)

@router.post('/new-exam/{course_id}', status_code=status.HTTP_201_CREATED, response_model=ExamsBase)
def add(course_id, exam: ExamsBase, db: Session = Depends(get_db)):
  new_exam = Exams(
    course_id = course_id,
    title = exam.title,
    duration_minutes = exam.duration_minutes,
    start_time = exam.start_time,
    end_time = exam.end_time,
    is_active = exam.is_active
  )
  
  db.add(new_exam)
  db.commit()
  db.refresh(new_exam)
  
  return new_exam

@router.get('/')
def aEll(db: Session = Depends(get_db)):
  exams =  db.query(Exams).all()
  return {
      'id': exams[0]['course_id']
          }