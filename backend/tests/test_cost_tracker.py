from backend.app.metrics.cost_tracker import (
    CostTracker
)

tracker = CostTracker()

tracker.track(
    "Research Redis",
    {
        "name": "TinyLLM",
        "cost_per_call": 0.0001
    }
)

tracker.track(
    "Compare Redis vs PostgreSQL",
    {
        "name": "Mistral",
        "cost_per_call": 0.001
    }
)

print(
    tracker.get_records()
)

print()

print(
    tracker.get_total_cost()
)