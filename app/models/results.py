from sqlalchemy import Integer,Column, Boolean, Time, ForeignKey

from app.database.db import Base

class Results(Base):
  __tablename__ = 'results'
  
  result_id = Column(Integer, primary_key=True, index=True)
  student_id = Column(Integer, ForeignKey('students.student_id'))
  exam_id = Column(Integer, ForeignKey('exams.exam_id'))
  score = Column(Integer)
  total_questions = Column(Integer)
  submitted_at = Column(Time)