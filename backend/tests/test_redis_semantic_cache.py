from backend.app.cache.cache_manager import (
    CacheManager
)

manager = CacheManager()

manager.store(
    query="What is Redis?",
    embedding=[0.1, 0.2, 0.3],
    response="Redis is an in-memory database."
)

manager.cache.cache.clear()

result = manager.lookup(
    "What is Redis?",
    [0.1, 0.2, 0.3]
)

print(result)

print(
    "\nSaved Executions:\n"
)

print(
    manager.get_saved_executions()
)