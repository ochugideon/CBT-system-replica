
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.routes import students as sr
from app.routes import questions as qr
from app.routes import exams as er
from app.routes import courses as cr
from app.routes import departments as dr
from app.routes import auth as ar

from app.models.students import Students
from app.schemas.deptartments import Departments
from app.models.departments import Departments as DepartmentModel



from app.database.db import engine, get_db
from app.models import courses, exams, questions, registered_students, results, students, departments


app = FastAPI(
  title = 'CBT Examination Management System'
)

courses.Base.metadata.create_all(engine)
exams.Base.metadata.create_all(engine)
questions.Base.metadata.create_all(engine)
registered_students.Base.metadata.create_all(engine)
results.Base.metadata.create_all(engine)
students.Base.metadata.create_all(engine)
departments.Base.metadata.create_all(engine)

app.include_router(ar.router)
app.include_router(sr.router)
app.include_router(qr.router)
app.include_router(er.router)
app.include_router(cr.router)
app.include_router(dr.router)


origins = [
    "http://127.0.0.1:5500",
    "https://yourdomain.com",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

@app.get('/')
def home():
  return {
    'message': 'API is running successfully.'
  }


  
@app.post('/departments')
def create_department(dept: Departments, db: Session = Depends(get_db)):
  dept_obj = DepartmentModel(
    name=dept.name,
    faculty=dept.faculty
  )
  db.add(dept_obj)
  db.commit()
  db.refresh(dept_obj)
  return dept_obj


