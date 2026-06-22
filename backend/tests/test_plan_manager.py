import uuid

from backend.app.agents.planning_agent import PlanningAgent

from backend.app.state.plan_manager import PlanManager

def main():
    workflow_id = str(uuid.uuid4())

    planner = PlanningAgent()
    manager = PlanManager()

    plan = planner.create_plan(
        "Research Redis and compare PostgreSQL"
    )

    manager.save_plan(workflow_id, plan)

    manager.save_task_result(
        workflow_id,
        1,
        "Redis is an in-memory datastore"
    )

    updated_plan = manager.get_plan(workflow_id)

    print(f"\nWorkflow ID: {workflow_id}\n")

    print("Updated Plan:\n")

    for task in updated_plan:
        print(task)

    ready_tasks = manager.get_ready_tasks(
         workflow_id
    )

    print("\nReady Tasks:\n")

    for task in ready_tasks:
        print(task)


if __name__ == "__main__":
    main()