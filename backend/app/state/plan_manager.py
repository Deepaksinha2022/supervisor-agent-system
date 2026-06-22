import json

from backend.app.core.redis_client import redis_client


class PlanManager:

    def __init__(self):
        self.redis = redis_client

    def save_plan(self, workflow_id: str, plan: list):
        key = f"plan:{workflow_id}"
        self.redis.set(key, json.dumps(plan))

    def get_plan(self, workflow_id: str):
        key = f"plan:{workflow_id}"

        data = self.redis.get(key)

        if not data:
            return None

        return json.loads(data)

    def update_task_status(
        self,
        workflow_id: str,
        task_id: int,
        status: str
    ):
        plan = self.get_plan(workflow_id)

        if not plan:
            return

        for task in plan:
            if task["task_id"] == task_id:
                task["status"] = status
                break

        self.save_plan(workflow_id, plan)

    def get_next_pending_task(self, workflow_id: str):
        plan = self.get_plan(workflow_id)

        if not plan:
            return None

        for task in plan:
            if (
                task["status"] == "pending"
                and self.dependencies_completed(
                workflow_id,
                task
                )
            ):
                return task

        return None

    def is_plan_completed(self, workflow_id: str):
        plan = self.get_plan(workflow_id)

        if not plan:
            return False

        return all(
            task["status"] == "completed"
            for task in plan
        )
    
    def save_task_result(
        self,
        workflow_id: str,
        task_id: int,
        result: str
        ):
        plan = self.get_plan(workflow_id)

        if not plan:
            return

        for task in plan:
            if task["task_id"] == task_id:
                task["result"] = result
                break

        self.save_plan(workflow_id, plan)

    def dependencies_completed(
            self,
            workflow_id: str,
            task
        ):

        plan = self.get_plan(workflow_id)

        completed_tasks = {
            t["task_id"]
            for t in plan
            if t["status"] == "completed"
        }

        return all(
            dep in completed_tasks
            for dep in task["depends_on"]
        )
    
    def get_ready_tasks(
        self,
        workflow_id: str
        ):

        plan = self.get_plan(workflow_id)

        if not plan:
            return []

        ready_tasks = []

        for task in plan:

            if (
                task["status"] == "pending"
                and self.dependencies_completed(
                    workflow_id,
                    task
                )
            ):
                ready_tasks.append(task)

        return ready_tasks
    
    def save_task_metric(
            self,
            workflow_id,
            task_id,
            metric_name,
            metric_value
        ):

        plan = self.get_plan(
            workflow_id
        )

        for task in plan:

            if task["task_id"] == task_id:

                if "metrics" not in task:
                    task["metrics"] = {}

                task["metrics"][
                    metric_name
                ] = metric_value

                break

        self.save_plan(
            workflow_id,
            plan
        )

    def increment_retry_count(
        self,
        workflow_id,
        task_id
    ):

        plan = self.get_plan(
            workflow_id
        )

        for task in plan:

            if task["task_id"] == task_id:

                task["retry_count"] += 1
                break

        self.save_plan(
            workflow_id,
            plan
        )

    def requeue_failed_tasks(
            self,
            workflow_id,
            max_retries=3
        ):

        plan = self.get_plan(
            workflow_id
        )

        for task in plan:

            if (
                task["status"] == "failed"
                and task["retry_count"] < max_retries
            ):
                task["status"] = "pending"

        self.save_plan(
            workflow_id,
            plan
        )

    def workflow_failed(
            self,
            workflow_id
        ):

        plan = self.get_plan(
            workflow_id
        )

        for task in plan:

            if (
                task["status"] == "failed"
                and task["retry_count"] >= 3
            ):
                return True

        return False
    
    def workflow_completed(
            self,
            workflow_id
        ):

        plan = self.get_plan(
            workflow_id
        )

        return all(
            task["status"] == "completed"
            for task in plan
        )
    
    def get_workflow_summary(
            self,
            workflow_id
        ):

        plan = self.get_plan(
            workflow_id
        )

        total_tasks = len(plan)

        completed_tasks = len(
            [
                task
                for task in plan
                if task["status"] == "completed"
            ]
        )

        failed_tasks = len(
            [
                task
                for task in plan
                if task["status"] == "failed"
            ]
        )

        total_execution_time = sum(
            task.get(
                "metrics",
                {}
            ).get(
                "execution_time",
                0
            )
            for task in plan
        )

        return {
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "failed_tasks": failed_tasks,
            "total_execution_time": total_execution_time
        }