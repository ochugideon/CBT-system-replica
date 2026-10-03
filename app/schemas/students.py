from pydantic import BaseModel


class RegisteredStudentsBase(BaseModel):
  access_code_hash: str
  # is_used: bool = False
  registered_at: str
  
  class Config:
    from_attributes = False

class RegisteredStudentShow(BaseModel):
  reg_number: str
  exam_id: int
  access_code_hash: str
  is_used: bool = False
  
  class Config:
    from_attributes = False

class StudentBase(BaseModel):
  reg_number: str
  
  class Config:
    from_attributes = False
    
class Login(BaseModel):
  reg_num: str
  access_code: str
  exam_id: int
  
class Token(BaseModel):
  access_token: str
  token_type: str
