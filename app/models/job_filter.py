from sqlalchemy import Column, Integer, String, JSON, Boolean
from app.db import Base

class JobFilter(Base):
    __tablename__ = "job_filters"

    id = Column(Integer, primary_key=True, index=True)
    keywords = Column(JSON, nullable=False, default=[])
    locations = Column(JSON, nullable=True, default=[])
    min_salary = Column(Integer, nullable=True)
    max_salary = Column(Integer, nullable=True)
    job_types = Column(JSON, nullable=False, default=["Full-time"])
    remote_only = Column(Boolean, default=False)
