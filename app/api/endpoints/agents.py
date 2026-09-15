from fastapi import APIRouter, Depends, BackgroundTasks
from typing import Dict, Any
from app.agents.hunter import HunterAgent
from app.agents.executive import ExecutiveAgent
from app.agents.verifier import VerifierAgent
from pydantic import BaseModel

class AuditRequest(BaseModel):
    change_description: str
    diff_content: str
    gate_results: Dict[str, Any]

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

@router.post("/verifier/audit")
async def run_audit(request: AuditRequest):
    """
    The Verifier Agent audits a proposed change against the Project Manifest.
    Returns a verdict (PASSED/REJECTED) and findings.
    """
    verifier = VerifierAgent()
    result = await verifier.audit_change(
        request.change_description,
        request.diff_content,
        request.gate_results
    )
    return result
