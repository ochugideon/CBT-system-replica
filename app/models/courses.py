from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey, JSON

from app.database.db import Base

class Courses(Base):
  __tablename__ = 'courses'
  
  course_id = Column(Integer, primary_key=True, index=True)
  course_code = Column(String, nullable=False)
  course_title = Column(String, nullable=False)
