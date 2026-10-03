import os
from dotenv import load_dotenv

load_dotenv(override=True)

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

url = os.getenv('SQL_DB_URL')

engine = create_engine(
  url,
  connect_args={
    'check_same_thread': False
  }
)

SessionLocal = sessionmaker(
  bind=engine,
  autoflush=False,
  autocommit=False
)

Base = declarative_base()

def get_db():
  db = SessionLocal()
  
  try:
    yield db
  finally:
    db.close()