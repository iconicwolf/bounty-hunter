import asyncio
import logging
from app.agents.executive import ExecutiveAgent
from app.agents.designer import DesignerAgent

# Setup logging to see the agent output
logging.basicConfig(level=logging.INFO)

async def test_executive():
    print("\n--- Testing Executive Agent ---")
    exec_agent = ExecutiveAgent()

    # Test 1: Requirement Analysis
    requirement = "I want to hunt for new jobs and ensure the system is secure"
    plan = await exec_agent.analyze_requirements(requirement)
    print(f"Requirement: {requirement}")
    print(f"Planned Tasks: {plan['planned_tasks']}")

    # Test 2: Full Orchestration Cycle
    # This will trigger Hunter -> Adversary -> Refiner (if needed) -> Approval
    print("\nRunning full orchestration cycle...")
    result = await exec_agent.orchestrate_cycle(requirement)
    print(f"Executive Result: {result}")

async def test_designer():
    print("\n--- Testing Designer Agent ---")
    design_agent = DesignerAgent()

    # Test 1: Design Spec Generation
    component = "Executive Dashboard"
    spec = await design_agent.generate_design_spec(component)
    print(f"Generated Spec for {component}:")
    print(f"  Palette: {spec['palette']}")
    print(f"  Typography: {spec['typography']}")

    # Test 2: Branding Audit
    css_sample = "body { background-color: #0A192F; color: #CCD6F6; }"
    findings = await design_agent.audit_branding(css_sample)
    print(f"Branding Audit Findings: {findings}")

async def main():
    try:
        await test_executive()
        await test_designer()
        print("\n✅ All governance agent tests passed successfully!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    asyncio.run(main())
