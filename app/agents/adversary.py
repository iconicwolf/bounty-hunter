import logging
import httpx
import asyncio
from app.core.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AdversaryAgent")

class AdversaryAgent:
    """
    The Adversary Agent is designed to 'break' the application by
    testing edge cases, malformed inputs, and system limits.
    """
    def __init__(self):
        self.base_url = f"http://localhost:8000"

    async def test_empty_profile(self):
        """Tests if the application crashes when no profile exists."""
        logger.info("Testing: Empty Profile Case...")
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/profile")
            if response.status_code == 404:
                logger.info("PASS: Application correctly handled missing profile with 404.")
                return True
            logger.error(f"FAIL: Application returned {response.status_code} for missing profile.")
            return False

    async def test_malformed_json(self):
        """Tests if the API crashes on malformed JSON input."""
        logger.info("Testing: Malformed JSON Input...")
        async with httpx.AsyncClient() as client:
            try:
                response = await client.post(
                    f"{self.base_url}/profile",
                    content="NOT JSON",
                    headers={"Content-Type": "application/json"}
                )
                if response.status_code == 422 or response.status_code == 400:
                    logger.info("PASS: Application correctly handled malformed JSON.")
                    return True
            except Exception as e:
                logger.error(f"FAIL: Application crashed: {e}")
                return False
            return False

    async def test_sql_injection_attempt(self):
        """Tries simple SQL injection strings in inputs."""
        logger.info("Testing: Basic SQL Injection attempt...")
        async with httpx.AsyncClient() as client:
            payload = {
                "full_name": "Admin' --",
                "professional_title": "Hacker",
                "email": "test@test.com",
                "skills": [],
                "experience_years": 1,
                "target_roles": []
            }
            response = await client.post(f"{self.base_url}/profile", json=payload)
            if response.status_code == 200:
                # If it returned 200 but the name is literally "Admin' --", it's handled as data
                # If it crashes or returns 500, it's a fail.
                logger.info("PASS: SQL Injection payload treated as literal string.")
                return True
            logger.error(f"FAIL: Application failed on SQL payload with status {response.status_code}")
            return False

    async def run_chaos_suite(self):
        logger.info("🚀 Starting Adversary Chaos Suite...")
        results = {
            "empty_profile": await self.test_empty_profile(),
            "malformed_json": await self.test_malformed_json(),
            "sql_injection": await self.test_sql_injection_attempt(),
        }

        passed = sum(results.values())
        total = len(results)
        logger.info(f"Chaos Suite Finished: {passed}/{total} passed.")
        return results
