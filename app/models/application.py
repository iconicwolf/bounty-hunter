from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Enum
from sqlalchemy.sql import func
import enum
from app.db import Base

class AppStatus(enum.Enum):
    WISHLIST = "Wishlist"
    APPLIED = "Applied"
    INTERVIEWING = "Interviewing"
    OFFER = "Offer"
    REJECTED = "Rejected"

class Application(Base):
    __tablename__ = "applications"

    id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    role_title = Column(String, nullable=False)
    job_url = Column(String, nullable=True)
    status = Column(Enum(AppStatus), default=AppStatus.WISHLIST)
    salary_range = Column(String, nullable=True)
    date_applied = Column(DateTime(timezone=True), server_default=func.now())
    follow_up_date = Column(DateTime(timezone=True), nullable=True)
    contact_person = Column(String, nullable=True)
    material_used = Column(Text, nullable=True)
    notes = Column(Text, nullable=True)
    evidence_path = Column(String, nullable=True) # Path to the captured screenshot
