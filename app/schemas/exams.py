from pydantic import BaseModel

class ExamsBase(BaseModel):
  title: str
  duration_minutes: str
  start_time: str
  end_time: str
  is_active: bool = False
  
  class Config:
    from_attributes = False
    
class ExamsShow(ExamsBase):
  title: str
  duration_minutes: str
  start_time: str
  end_time: str
  is_active: bool = False
  course_id: int
  
  class Config:
    from_attributes = False