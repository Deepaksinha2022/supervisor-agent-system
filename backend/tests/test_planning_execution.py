import asyncio
import uuid

from backend.app.agents.planning_agent import PlanningAgent
from backend.app.agents.supervisor_agent import SupervisorAgent
from backend.app.state.plan_manager import PlanManager


async def main():

    workflow_id = str(uuid.uuid4())

    planner = PlanningAgent()
    manager = PlanManager()
    supervisor = SupervisorAgent()

    plan = planner.create_plan(
        "Research Redis and compare PostgreSQL"
    )

    manager.save_plan(
        workflow_id,
        plan
    )

    final_plan = await supervisor.execute_plan(
        workflow_id,
        manager
    )

    print(f"\nWorkflow ID: {workflow_id}\n")

    print("Final Plan:\n")

    for task in final_plan:
        print(task)


if __name__ == "__main__":
    asyncio.run(main())