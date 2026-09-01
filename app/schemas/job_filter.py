from pydantic import BaseModel, Field
from typing import List, Optional

class JobFilterBase(BaseModel):
    keywords: List[str] = Field(default=[], description="Keywords to search for (e.g., 'Python', 'Remote')")
    locations: List[str] = Field(default=[], description="Locations to target")
    min_salary: Optional[int] = None
    max_salary: Optional[int] = None
    job_types: List[str] = Field(default=["Full-time"], description="Full-time, Part-time, Contract")
    remote_only: bool = False

class JobFilterCreate(JobFilterBase):
    pass

class JobFilterRead(JobFilterBase):
    id: int

    class Config:
        from_attributes = True
