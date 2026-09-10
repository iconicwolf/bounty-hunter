from fastapi import APIRouter, Depends, BackgroundTasks
from app.agents.hunter import HunterAgent
from app.agents.executive import ExecutiveAgent
from app.agents.designer import DesignerAgent

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

@router.post("/executive/orchestrate")
async def trigger_executive(requirement: str, background_tasks: BackgroundTasks):
    """
    Trigger the Executive Agent to orchestrate the entire Enterprise Loop
    based on a high-level requirement.
    """
    executive = ExecutiveAgent()
    background_tasks.add_task(executive.orchestrate_cycle, requirement)
    return {"message": f"Executive Agent is orchestrating the Enterprise Loop for: {requirement}"}

@router.get("/designer/spec/{component}")
async def get_design_spec(component: str):
    """
    Get the professional design specification for a UI component from the Designer Agent.
    """
    designer = DesignerAgent()
    spec = await designer.generate_design_spec(component)
    return spec

@router.get("/designer/suggestions")
async def get_ui_suggestions():
    """
    Get proactive UI/UX improvement suggestions from the Designer Agent based on current model fields.
    """
    designer = DesignerAgent()
    # Use current Application model fields for analysis
    current_fields = ["company_name", "role_title", "date_applied", "status", "job_url", "match_score", "evidence_path"]
    return await designer.suggest_ui_improvements(current_fields)
