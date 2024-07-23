from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter()

@router.post("/")
def create_course(name: str, degree_id: int, db: Session = Depends(get_db)):
    degree = db.query(models.Degree).filter(models.Degree.id == degree_id).first()
    
    if degree is None:
        raise HTTPException(status_code=400, detail="Degree with the provided ID does not exist")

    db_course = models.Course(name=name, degree_id=degree_id)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    return db_course