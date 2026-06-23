import json

from backend.app.core.redis_client import (
    redis_client
)


class RedisCache:

    def set(
        self,
        key,
        value,
        ttl=86400
    ):

        redis_client.setex(
            key,
            ttl,
            json.dumps(value)
        )

    def get(
        self,
        key
    ):

        data = redis_client.get(
            key
        )

        if not data:
            return None

        return json.loads(
            data
        )

    def delete(
        self,
        key
    ):

        redis_client.delete(
            key
        )

    def keys(
        self,
        pattern="*"
    ):

        return redis_client.keys(
            pattern
        )