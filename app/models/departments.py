from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey, JSON

from app.database.db import Base

class Departments(Base):
  __tablename__ = 'departments'
  
  dept_id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  faculty = Column(String)