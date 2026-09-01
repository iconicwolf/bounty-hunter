from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db import get_db
from app.models.user_profile import UserProfile
from app.schemas.user_profile import UserProfileCreate, UserProfileRead

router = APIRouter(prefix="/profile", tags=["Profile"])

@router.get("/", response_model=UserProfileRead)
async def get_profile(db: Session = Depends(get_db)):
    profile = db.query(UserProfile).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Professional profile not set up yet")
    return profile

@router.post("/", response_model=UserProfileRead)
async def set_profile(profile: UserProfileCreate, db: Session = Depends(get_db)):
    # Update existing profile or create new one
    existing_profile = db.query(UserProfile).first()
    if existing_profile:
        for key, value in profile.model_dump().items():
            setattr(existing_profile, key, value)
        db.commit()
        db.refresh(existing_profile)
        return existing_profile

    db_profile = UserProfile(**profile.model_dump())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
