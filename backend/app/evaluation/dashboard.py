class Dashboard:

    def generate(
        self,
        benchmark_summary,
        cost_tracker,
        cache_metrics
    ):

        return {
            "total_workflows":
                benchmark_summary[
                    "total_workflows"
                ],

            "average_latency":
                benchmark_summary[
                    "average_latency"
                ],

            "success_rate":
                benchmark_summary[
                    "success_rate"
                ],

            "total_cost":
                cost_tracker.get_total_cost(),

            "cache_hits":
                cache_metrics[
                    "cache_hits"
                ],

            "cache_misses":
                cache_metrics[
                    "cache_misses"
                ]
        }