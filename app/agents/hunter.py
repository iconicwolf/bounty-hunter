import logging
from typing import List, Dict, Any
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models.user_profile import UserProfile
from app.models.job_filter import JobFilter
from app.models.application import Application, AppStatus
from app.core.config import settings
from serpapi import GoogleSearch

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("HunterAgent")

class HunterAgent:
    def __init__(self):
        self.db = SessionLocal()

    def get_search_params(self) -> Dict[str, Any]:
        profile = self.db.query(UserProfile).first()
        job_filter = self.db.query(JobFilter).first()

        if not profile:
            logger.error("User profile not found. Please set up your profile in the UI.")
            return None

        # Combine target roles from profile and keywords from filter
        keywords = job_filter.keywords if job_filter else profile.target_roles
        locations = job_filter.locations if job_filter else ["Remote"]

        return {
            "keywords": keywords,
            "locations": locations,
            "profile": profile
        }

    async def search_jobs(self) -> List[Dict[str, Any]]:
        params = self.get_search_params()
        if not params:
            return []

        query = " ".join(params['keywords'])
        location = ", ".join(params['locations'])

        logger.info(f"Sourcing live jobs for: {query} in {location}")

        try:
            search = GoogleSearch({
                "engine": "google_jobs",
                "q": query,
                "l": location,
                "api_key": settings.SERPAPI_KEY
            })
            results = search.get_dict()
            jobs_results = results.get("jobs_results", [])

            parsed_jobs = []
            for job in jobs_results:
                parsed_jobs.append({
                    "company": job.get("company_name"),
                    "role": job.get("title"),
                    "url": job.get("related_links", [{}])[0].get("link", "N/A") if job.get("related_links") else "N/A",
                    "description": job.get("description"),
                    "location": job.get("location")
                })
            return parsed_jobs

        except Exception as e:
            logger.error(f"Error sourcing jobs from SerpApi: {e}")
            return []

    async def analyze_and_track(self, jobs: List[Dict[str, Any]]):
        profile = self.db.query(UserProfile).first()

        for job in jobs:
            if not job['company'] or not job['role']:
                continue

            match_score = 0
            description = (job['description'] or "").lower()
            for skill in profile.skills:
                if skill.lower() in description:
                    match_score += 1

            if match_score > 0:
                logger.info(f"Match Found: {job['role']} at {job['company']} (Score: {match_score})")

                exists = self.db.query(Application).filter(
                    Application.job_url == job['url']
                ).first()

                if not exists:
                    new_app = Application(
                        company_name=job['company'],
                        role_title=job['role'],
                        job_url=job['url'],
                        status=AppStatus.WISHLIST,
                        notes=f"Auto-found by Hunter Agent. Match Score: {match_score}"
                    )
                    self.db.add(new_app)

        self.db.commit()

    async def run_cycle(self):
        logger.info("Starting BountyHunter sourcing cycle...")
        jobs = await self.search_jobs()
        await self.analyze_and_track(jobs)
        logger.info(f"Hunter Agent cycle complete. Processed {len(jobs)} jobs.")
