from backend.app.state.plan_manager import (
    PlanManager
)

workflow_id = input(
    "Workflow ID: "
)

manager = PlanManager()

manager.approve_task(
    workflow_id,
    1
)

manager.approve_task(
    workflow_id,
    2
)

print(
    manager.get_plan(
        workflow_id
    )
)