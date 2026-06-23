class BenchmarkSuite:

    def __init__(self):

        self.results = []

    def record(
        self,
        workflow_id,
        execution_time,
        success
    ):

        self.results.append(
            {
                "workflow_id": workflow_id,
                "execution_time": execution_time,
                "success": success
            }
        )

    def average_latency(
        self
    ):

        if not self.results:

            return 0

        total = sum(
            item["execution_time"]
            for item in self.results
        )

        return (
            total
            / len(
                self.results
            )
        )

    def success_rate(
        self
    ):

        if not self.results:

            return 0

        successful = sum(
            1
            for item in self.results
            if item["success"]
        )

        return (
            successful
            / len(
                self.results
            )
        ) * 100

    def summary(
        self
    ):

        return {
            "total_workflows":
                len(
                    self.results
                ),
            "average_latency":
                self.average_latency(),
            "success_rate":
                self.success_rate()
        }