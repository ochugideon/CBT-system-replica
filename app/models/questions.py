from sqlalchemy import Integer,Column,String, Boolean, Time, ForeignKey, JSON

from app.database.db import Base

class Questions(Base):
  __tablename__ = 'questions'
  question_id = Column(Integer, primary_key=True, index=True)
  exam_id = Column(Integer, ForeignKey('exams.exam_id'))
  question_text = Column(String)
  options_json = Column(JSON)
  correct_option = Column(String)