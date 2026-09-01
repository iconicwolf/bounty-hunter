from fastapi import APIRouter, Depends, BackgroundTasks
from app.agents.hunter import HunterAgent

router = APIRouter(prefix="/agents", tags=["Agents"])

@router.post("/hunter/search")
async def trigger_hunter(background_tasks: BackgroundTasks):
    """
    Trigger the Hunter Agent to search for jobs based on your profile
    and filters, and add them to your application tracker.
    """
    hunter = HunterAgent()
    background_tasks.add_task(hunter.run_cycle)
    return {"message": "Hunter Agent has started searching for jobs in the background. Check /applications soon!"}
