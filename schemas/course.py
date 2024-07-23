from pydantic import BaseModel

class Course(BaseModel):
    name: str
    degree_id: int

class CourseResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True