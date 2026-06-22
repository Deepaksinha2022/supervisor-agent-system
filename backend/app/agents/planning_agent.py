from typing import List, Dict


class PlanningAgent:
    """
    Planning Agent

    Converts a user request into a structured plan.
    """

    def create_plan(self, query: str) -> List[Dict]:
        query = query.strip()

        tasks = []

        if "compare" in query.lower():
            parts = query.lower().split("compare")

            if len(parts) == 2:
                left = parts[0].replace("and", "").strip()
                right = parts[1].strip()

                tasks = [
                    f"Research {left}",
                    f"Research {right}",
                    "Compare Features",
                    "Generate Summary",
                ]
        else:
            tasks = [
                f"Research: {query}",
                "Generate Summary",
            ]

        plan = []

        for idx, task in enumerate(tasks, start=1):
            
            plan = []

            if len(tasks) == 4:

                plan.append(
                    {
                        "task_id": 1,
                        "task_name": tasks[0],
                        "status": "pending",
                        "result": None,
                        "depends_on": [],
                        "retry_count":0
                    }
                )

                plan.append(
                    {
                        "task_id": 2,
                        "task_name": tasks[1],
                        "status": "pending",
                        "result": None,
                        "depends_on": [],
                        "retry_count":0
                    }
                )

                plan.append(
                    {
                        "task_id": 3,
                        "task_name": tasks[2],
                        "status": "pending",
                        "result": None,
                        "depends_on": [1, 2],
                        "retry_count":0
                    }
                )

                plan.append(
                    {
                        "task_id": 4,
                        "task_name": tasks[3],
                        "status": "pending",
                        "result": None,
                        "depends_on": [3],
                        "retry_count":0
                    }
                )

            else:

                for idx, task in enumerate(tasks, start=1):

                    plan.append(
                        {
                            "task_id": idx,
                            "task_name": task,
                            "status": "pending",
                            "result": None,
                            "depends_on": []
                        }
                    )

            return plan