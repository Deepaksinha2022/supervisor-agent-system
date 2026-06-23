from backend.app.models.model_registry import (
    ModelRegistry
)

from backend.app.models.model_router import (
    ModelRouter
)


registry = ModelRegistry()

registry.register(
    "small_model",
    {
        "name": "TinyLLM",
        "cost_per_call": 0.0001,
        "latency_ms": 100
    }
)

registry.register(
    "medium_model",
    {
        "name": "Mistral",
        "cost_per_call": 0.001,
        "latency_ms": 500
    }
)

registry.register(
    "large_model",
    {
        "name": "Llama",
        "cost_per_call": 0.01,
        "latency_ms": 2000
    }
)

router = ModelRouter(
    registry
)

print(
    router.route(
        "2 + 2"
    )
)

print(
    router.route(
        "Compare Redis and PostgreSQL"
    )
)

print(
    router.route(
        "Design a distributed multi agent architecture"
    )
)