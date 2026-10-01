from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey, JSON

from app.database.db import Base

class Registered(Base):
  __tablename__ = 'registered'
  
  registration_id = Column(Integer, primary_key=True, index=True)
  student_id = Column(Integer, ForeignKey('students.student_id'))
  exam_id = Column(Integer, ForeignKey('exams.exam_id'))
  access_code_hash = Column(String)
  is_used = Column(Boolean, default=False)
  registered_at = Column(String)
