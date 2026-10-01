from pydantic import BaseModel

class CoursesBase(BaseModel):
  course_code: str
  course_title: str
  
  class Config:
    from_attributes = False