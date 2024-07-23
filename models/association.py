from sqlalchemy import Table, Column, Integer, ForeignKey
from database import Base

lead_course_association = Table(
    'lead_course_association',
    Base.metadata,
    Column('id', Integer, primary_key=True, index=True), 
    Column('lead_id', Integer, ForeignKey('leads.id')),
    Column('course_id', Integer, ForeignKey('courses.id'))
)