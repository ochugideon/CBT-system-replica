from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.students import Students as StudentModel
from app.models.questions import Questions, Options
from app.schemas.questions import QuestionsBase

router = APIRouter(
  prefix='/api/questions',
  tags=['Questions']
)

@router.post('/new-question/{exam_id}', status_code= status.HTTP_201_CREATED, response_model=QuestionsBase)
def add(exam_id,question: QuestionsBase, db: Session = Depends(get_db)):
  new_question = Questions(
    exam_id = exam_id,
    question_text = question.question_text
  )
  
  if len(question.options) < 4:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
      detail='each question should have atleast 4 options'
    )
  elif len(question.options) > 5:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
      detail='each question should have maximum 5 options'
    )
    
  db.add(new_question)
  db.commit()
  db.refresh(new_question)
  options = []
  for option in question.options:
    new_option = Options(
      option_text = option.option_text,
      is_correct = option.is_correct,
      question_id = new_question.question_id
    )
    options.append(new_option)
    
  db.bulk_save_objects(options)
  db.commit()
  
  return new_question

@router.get('/', response_model=List[QuestionsBase])
def all(db: Session = Depends(get_db)):
  return db.query(Questions).all()