from pydantic import BaseModel


class RegisteredStudentsBase(BaseModel):
  access_code_hash: str
  # is_used: bool = False
  registered_at: str
  
  class Config:
    from_attributes = False

class RegisteredStudentShow(BaseModel):
  student_id: int
  exam_id: int
  access_code_hash: str
  is_used: bool = False
  
  class Config:
    from_attributes = False

class StudentBase(BaseModel):
  reg_number: str
  
  class Config:
    from_attributes = False