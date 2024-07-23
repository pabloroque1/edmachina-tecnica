from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
import models
from database import get_db

router = APIRouter()

@router.post("/")
def create_degree(name: str, db: Session = Depends(get_db)):
    db_degree = models.Degree(name=name )
    db.add(db_degree)
    db.commit()
    db.refresh(db_degree)
    return db_degree

@router.get("/{degree_id}")
def get_degree_by_id(degree_id: int, db: Session = Depends(get_db)):
    degree = db.query(models.Degree).filter(models.Degree.id == degree_id).first()
    if degree is None:
        raise HTTPException(status_code=404, detail="Degree not found")
    return degree