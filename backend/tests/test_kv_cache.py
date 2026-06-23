from backend.app.cache.kv_cache import (
    KVCache
)

cache = KVCache()

cache.store(
    "session_1",
    "last_query",
    "What is Redis?"
)

cache.store(
    "session_1",
    "last_answer",
    "Redis is an in-memory database."
)

print(
    cache.get(
        "session_1",
        "last_query"
    )
)

print()

print(
    cache.get_session(
        "session_1"
    )
)

cache.delete_session(
    "session_1"
)

print()

print(
    cache.get_session(
        "session_1"
    )
)