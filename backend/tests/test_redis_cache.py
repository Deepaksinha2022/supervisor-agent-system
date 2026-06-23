from backend.app.cache.redis_cache import (
    RedisCache
)

cache = RedisCache()

cache.set(
    "redis_test",
    {
        "answer": "Hello Redis"
    }
)

print(
    cache.get(
        "redis_test"
    )
)

cache.delete(
    "redis_test"
)

print(
    cache.get(
        "redis_test"
    )
)