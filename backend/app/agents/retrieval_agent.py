from backend.app.rag.hybrid_retriever import (
    HybridRetriever
)

from langsmith import traceable


class RetrievalAgent:

    def __init__(self, chunks):

        self.retriever = HybridRetriever(
            chunks
        )

    @traceable
    async def retrieve(
        self,
        query: str
    ):

        results = await self.retriever.retrieve(
            query
        )

        return results