import uuid

from backend.app.state.plan_manager import (
    PlanManager
)


workflow_id = str(
    uuid.uuid4()
)

manager = PlanManager()

plan = [
    {
        "task_id": 1,
        "task_name": "Test Task",
        "status": "pending_approval"
    }
]

manager.save_plan(
    workflow_id,
    plan
)

manager.reject_task(
    workflow_id,
    1
)
print(
    manager.has_pending_approval(
        workflow_id
    )
)

print(
    manager.get_plan(
        workflow_id
    )
)