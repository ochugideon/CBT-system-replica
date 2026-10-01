from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey
from sqlalchemy.orm import relationship

from app.database.db import Base

class Questions(Base):
  __tablename__ = 'questions'
  question_id = Column(Integer, primary_key=True, index=True)
  exam_id = Column(Integer, ForeignKey('exams.exam_id'))
  question_text = Column(String)
  options = relationship('Options', back_populates='question')
  
class Options(Base):
  __tablename__ = 'options'
  
  option_id = Column(Integer, primary_key=True, index=True)
  option_text = Column(String)
  is_correct = Column(Boolean)
  question_id = Column(Integer, ForeignKey('questions.question_id'))
  question = relationship('Questions', back_populates='options')