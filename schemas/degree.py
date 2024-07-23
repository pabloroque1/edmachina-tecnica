from pydantic import BaseModel
from typing import List
from .course import Course

class Degree(BaseModel):
    name: str
    courses: List[Course] = []