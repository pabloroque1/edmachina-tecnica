from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from database import Base
from models.association import lead_course_association

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    last_name=Column(String)
    email=Column(String)
    address = Column(String)
    phone_number=Column(Integer)
    course_time_months = Column(Integer)
    year_of_inscription = Column(Integer)
    times_of_take_course = Column(Integer)
    courses = relationship('Course', secondary=lead_course_association, back_populates='leads')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)