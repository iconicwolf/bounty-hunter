from pydantic import BaseModel, EmailStr, HttpUrl
from typing import List, Optional

class UserProfileBase(BaseModel):
    full_name: str
    professional_title: str
    email: EmailStr
    skills: List[str]
    experience_years: int
    bio: Optional[str] = None
    github_url: Optional[HttpUrl] = None
    linkedin_url: Optional[HttpUrl] = None
    portfolio_url: Optional[HttpUrl] = None
    target_roles: List[str]
    preferred_locations: Optional[List[str]] = None
    min_salary: Optional[int] = None
    top_achievements: Optional[List[str]] = None

class UserProfileCreate(UserProfileBase):
    pass

class UserProfileRead(UserProfileBase):
    id: int

    class Config:
        from_attributes = True
