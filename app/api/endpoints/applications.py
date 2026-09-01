from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.application import Application
from app.schemas.application import ApplicationCreate, ApplicationRead

router = APIRouter(prefix="/applications", tags=["Applications"])

@router.get("/", response_model=List[ApplicationRead])
async def read_applications(db: Session = Depends(get_db)):
    return db.query(Application).all()

@router.post("/", response_model=ApplicationRead, status_code=201)
async def create_application(app_data: ApplicationCreate, db: Session = Depends(get_db)):
    db_app = Application(**app_data.model_dump())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

@router.delete("/{app_id}")
async def delete_application(app_id: int, db: Session = Depends(get_db)):
    db_app = db.query(Application).filter(Application.id == app_id).first()
    if not db_app:
        raise HTTPException(status_code=404, detail="Application not found")
    db.delete(db_app)
    db.commit()
    return {"message": "Application deleted successfully"}
