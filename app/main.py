from fastapi import FastAPI

from app.database.db import engine
from app.models import courses, exams, questions, registered_students, results, students, departments


app = FastAPI(
  title = 'CBT Examination Management System'
)

@app.get('/')
def home():
  return {
    'message': 'API is running successfully.'
  }

courses.Base.metadata.create_all(engine)
exams.Base.metadata.create_all(engine)
questions.Base.metadata.create_all(engine)
registered_students.Base.metadata.create_all(engine)
results.Base.metadata.create_all(engine)
students.Base.metadata.create_all(engine)
departments.Base.metadata.create_all(engine)