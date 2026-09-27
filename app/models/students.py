from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey, JSON

from app.database.db import Base

class Students(Base):
  __tablename__ = 'students'
  
  student_id = Column(Integer, primary_key=True, index=True)
  reg_number = Column(String, unique=True)
  full_name = Column(String)
  department_id = Column(Integer, ForeignKey('departments.dept_id'))
