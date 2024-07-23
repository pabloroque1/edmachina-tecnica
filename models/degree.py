from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from database import Base

class Degree(Base):
    __tablename__ = "degrees"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String)
    courses = relationship('Course', back_populates='degree')

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)