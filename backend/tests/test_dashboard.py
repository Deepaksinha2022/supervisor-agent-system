from backend.app.evaluation.dashboard import (
    Dashboard
)

from backend.app.evaluation.benchmark_suite import (
    BenchmarkSuite
)

from backend.app.metrics.cost_tracker import (
    CostTracker
)


benchmark = BenchmarkSuite()

benchmark.record(
    "wf_1",
    1.2,
    True
)

benchmark.record(
    "wf_2",
    0.8,
    True
)


cost_tracker = CostTracker()

cost_tracker.track(
    "Research Redis",
    {
        "name": "TinyLLM",
        "cost_per_call": 0.0001
    }
)

cost_tracker.track(
    "Compare Databases",
    {
        "name": "Mistral",
        "cost_per_call": 0.001
    }
)


cache_metrics = {
    "cache_hits": 10,
    "cache_misses": 2
}


dashboard = Dashboard()

print(
    dashboard.generate(
        benchmark.summary(),
        cost_tracker,
        cache_metrics
    )
)