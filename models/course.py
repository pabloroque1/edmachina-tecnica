from sqlalchemy import Column, String, Integer, ForeignKey, Table
from database import Base
from sqlalchemy.orm import relationship
from models.association import lead_course_association

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    degree_id = Column(Integer, ForeignKey('degrees.id'))

    degree = relationship('Degree', back_populates='courses')
    leads = relationship('Lead', secondary=lead_course_association, back_populates='courses')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)