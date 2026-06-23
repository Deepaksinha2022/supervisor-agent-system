from backend.app.cache.cache_manager import (
    CacheManager
)

manager = CacheManager()

manager.store(
    query="What is Redis?",
    embedding=[0.1, 0.2, 0.3],
    response="Redis is an in-memory database."
)

result = manager.lookup(
    [0.1, 0.2, 0.3]
)

print(result)

print(
    manager.metrics()
)

cache = manager.cache

cache.cleanup_expired()

print(
    "\nCache Size:\n"
)

print(
    len(
        cache.get_all()
    )
)