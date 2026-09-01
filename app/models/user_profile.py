from sqlalchemy import Column, Integer, String, Text, JSON
from app.db import Base

class UserProfile(Base):
    __tablename__ = "user_profiles"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    professional_title = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    skills = Column(JSON, nullable=False) # List of skills
    experience_years = Column(Integer, default=0)
    bio = Column(Text, nullable=True)
    github_url = Column(String, nullable=True)
    linkedin_url = Column(String, nullable=True)
    portfolio_url = Column(String, nullable=True)
    target_roles = Column(JSON, nullable=False) # List of roles
    preferred_locations = Column(JSON, nullable=True) # List of locations
    min_salary = Column(Integer, nullable=True)
    top_achievements = Column(JSON, nullable=True) # List of achievements
