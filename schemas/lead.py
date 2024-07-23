from pydantic import BaseModel
from typing import List
from .course import CourseResponse

class LeadResponse(BaseModel):
    id: int
    name: str
    last_name: str
    email: str
    address: str
    phone_number: int
    course_time_months: int
    year_of_inscription: int
    times_of_take_course: int
    courses: List[CourseResponse]

    class Config:
        orm_mode = True



class Lead(BaseModel):

    name: str
    last_name: str
    email: str
    address: str
    phone_number: int
    course: str
    course_time_months: int
    year_of_inscription: int
    degree: str
    times_of_take_course: int
    course_ids: List[int]

    class Config:
        from_attributes = True