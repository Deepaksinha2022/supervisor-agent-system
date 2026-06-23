class CostTracker:

    def __init__(self):

        self.total_cost = 0

        self.records = []

    def track(
        self,
        task_name,
        model
    ):

        cost = model[
            "cost_per_call"
        ]

        self.total_cost += cost

        self.records.append(
            {
                "task": task_name,
                "model": model["name"],
                "cost": cost
            }
        )

    def get_total_cost(
        self
    ):

        return self.total_cost

    def get_records(
        self
    ):

        return self.records