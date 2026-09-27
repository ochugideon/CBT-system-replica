from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey, JSON

from app.database.db import Base

class Exams(Base):
  __tablename__ = 'exams'
  
  exam_id = Column(Integer, primary_key=True, index=True)
  course_id = Column(Integer, ForeignKey('courses.course_id'))
  title = Column(String)
  duration_minutes = Column(String)
  start_time = Column(Time)
  end_time = Column(Time)
  is_active = Column(Boolean)
