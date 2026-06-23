import numpy as np

from datetime import datetime, timedelta

class SemanticCache:

    def __init__(self):

        self.cache = []

        self.cache_hits = 0

        self.cache_misses = 0

    def add(
        self,
        query,
        embedding,
        response
    ):

        self.cache.append(
            {
            "query": query,
            "embedding": embedding,
            "response": response,
            "created_at": (
                datetime.utcnow()
                .isoformat()
            )
        }
        )

    def get_all(
        self
    ):

        return self.cache
    
    def cosine_similarity(
            self,
            vec1,
            vec2
        ):

        vec1 = np.array(
            vec1
        )

        vec2 = np.array(
            vec2
        )

        return np.dot(
            vec1,
            vec2
        ) / (
            np.linalg.norm(vec1)
            * np.linalg.norm(vec2)
        )
    
    def search(
            self,
            embedding,
            threshold=0.90
        ):

        best_match = None

        best_score = 0

        for item in self.cache:

            if self.is_expired(item):
                 continue

            similarity = (
                self.cosine_similarity(
                    embedding,
                    item["embedding"]
                )
            )

            if (
                similarity > best_score
                and similarity >= threshold
            ):

                best_score = similarity

                best_match = item

        if best_match:

            self.cache_hits += 1

            return {
                "cache_hit": True,
                "response": best_match
            }

        self.cache_misses += 1

        return {
            "cache_hit": False,
            "response": None
        }
    
    def get_metrics(
            self
        ):

        return {
            "cache_hits": self.cache_hits,
            "cache_misses": self.cache_misses
        }
    
    def hit_rate(
        self
        ):

        total = (
            self.cache_hits
            + self.cache_misses
        )

        if total == 0:
            return 0

        return (
            self.cache_hits
            / total
        ) * 100
    
    def is_expired(
        self,
        item,
        ttl_hours=24
        ):

        created_at = datetime.fromisoformat(
            item["created_at"]
        )

        return (
            datetime.utcnow()
            >
            created_at
            + timedelta(
                hours=ttl_hours
            )
        )
    
    def cleanup_expired(
            self,
            ttl_hours=24
        ):

        self.cache = [

            item

            for item in self.cache

            if not self.is_expired(
                item,
                ttl_hours
            )
        ]