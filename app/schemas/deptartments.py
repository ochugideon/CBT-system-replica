from pydantic import BaseModel

class Departments(BaseModel):
    name: str
    faculty: str

    class Config:
        from_attributes = True