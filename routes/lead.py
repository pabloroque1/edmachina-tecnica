from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
import schemas
import models
from database import get_db


router = APIRouter()

@router.post("/")
def create_lead(lead: schemas.Lead, db: Session = Depends(get_db)):
    db_courses = db.query(models.Course).filter(models.Course.id.in_(lead.course_ids)).all()

    if len(db_courses) != len(lead.course_ids):
        raise HTTPException(status_code=404, detail="One or more courses not found")

    db_lead = models.Lead(
        name=lead.name,
        last_name=lead.last_name,
        email=lead.email,
        address=lead.address,
        phone_number=lead.phone_number,
        course_time_months=lead.course_time_months,
        year_of_inscription=lead.year_of_inscription,
        times_of_take_course=lead.times_of_take_course,
        courses=db_courses
    )
    
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

@router.get("/", response_model=List[schemas.LeadResponse])
async def get_leads(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    leads = db.query(models.Lead).offset(skip).limit(limit).all()
    return leads

@router.get("/{lead_id}", response_model=schemas.LeadResponse)
async def get_lead(lead_id: int, db: Session = Depends(get_db)):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if lead is None:
        raise HTTPException(status_code=404, detail="Lead not found")
    return lead