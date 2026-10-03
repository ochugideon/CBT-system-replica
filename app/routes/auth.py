from fastapi import APIRouter, Depends, status, HTTPException, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm
from typing import List
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database.db import get_db
from app.models.registered_students import Registered as RegisteredStudentModel
from app.schemas.students import RegisteredStudentShow
from app.schemas.students import Login, Token

from app.settings.token import create_access_token

router = APIRouter(
  prefix='/api/v1/auth/exam-login',
  tags=['Login']
)

@router.post('', response_model=Token)
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
  student = db.query(RegisteredStudentModel).filter_by(
    reg_number=request.username.upper()
    ).first()
  
  if not student:
    raise HTTPException(
      status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
      detail='invalid reg number'
    )
  if not student.access_code_hash == request.password:
      raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,
        detail='invalid password.'
      )
  
  access_token = create_access_token(
    data={"reg_number": request.username, 'access_token': request.password})
  
  return Token(
    access_token=access_token,
    token_type="bearer"
  )
