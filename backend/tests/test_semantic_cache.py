from backend.app.cache.semantic_cache import (
    SemanticCache
)

cache = SemanticCache()

cache.add(
    query="What is Redis?",
    embedding=[0.1, 0.2, 0.3],
    response="Redis is an in-memory database."
)

print(
    cache.get_all()
)

result = cache.search(
    [0.1, 0.2, 0.3]
    )

print(
        "\nCache Hit:\n"
    )

print(result)

print(
    "\nMetrics:\n"
)

print(
    cache.get_metrics()
)

print(
    "\nHit Rate:\n"
)

print(
    cache.hit_rate()
)