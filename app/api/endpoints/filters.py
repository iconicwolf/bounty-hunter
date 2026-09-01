from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.job_filter import JobFilter
from app.schemas.job_filter import JobFilterCreate, JobFilterRead

router = APIRouter(prefix="/filters", tags=["Filters"])

@router.get("/", response_model=JobFilterRead)
async def get_filter(db: Session = Depends(get_db)):
    filter_obj = db.query(JobFilter).first()
    if not filter_obj:
        # Return default filter if none exists
        return JobFilter(keywords=[], locations=[], job_types=["Full-time"], remote_only=False)
    return filter_obj

@router.post("/", response_model=JobFilterRead)
async def set_filter(filter_data: JobFilterCreate, db: Session = Depends(get_db)):
    existing_filter = db.query(JobFilter).first()
    if existing_filter:
        for key, value in filter_data.model_dump().items():
            setattr(existing_filter, key, value)
        db.commit()
        db.refresh(existing_filter)
        return existing_filter

    db_filter = JobFilter(**filter_data.model_dump())
    db.add(db_filter)
    db.commit()
    db.refresh(db_filter)
    return db_filter
