from backend.app.evaluation.benchmark_suite import (
    BenchmarkSuite
)

benchmark = BenchmarkSuite()

benchmark.record(
    workflow_id="wf_1",
    execution_time=1.2,
    success=True
)

benchmark.record(
    workflow_id="wf_2",
    execution_time=0.8,
    success=True
)

benchmark.record(
    workflow_id="wf_3",
    execution_time=2.0,
    success=False
)

print(
    benchmark.summary()
)