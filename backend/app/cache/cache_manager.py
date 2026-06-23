from backend.app.cache.semantic_cache import (
    SemanticCache
)

from backend.app.cache.redis_cache import (
    RedisCache
)


class CacheManager:

    def __init__(self):

        self.cache = SemanticCache()

        self.redis_cache = RedisCache()

        self.saved_executions = 0

    def lookup(
            self,
            query,
            embedding
        ):

            self.cache.cleanup_expired()

            result = self.cache.search(
                embedding
            )

            if result["cache_hit"]:

                self.saved_executions += 1

                return result

            redis_result = (
                self.redis_cache.get(
                    query
                )
            )

            if redis_result:

                self.saved_executions += 1

                return {
                    "cache_hit": True,
                    "response": redis_result
                }

            return {
                "cache_hit": False,
                "response": None
            }
    def store(
        self,
        query,
        embedding,
        response
    ):

        self.cache.add(
            query,
            embedding,
            response
        )

        self.redis_cache.set(
            query,
            {
                "query": query,
                "embedding": embedding,
                "response": response
            }
        )

    def load_from_redis(
        self,
        query
    ):

        return self.redis_cache.get(
            query
        )

    def metrics(
        self
    ):

        return self.cache.get_metrics()

    def get_saved_executions(
        self
    ):

        return self.saved_executions