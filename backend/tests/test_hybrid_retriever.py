import asyncio

from app.rag.hybrid_retriever import (
    HybridRetriever
)


class DummyChunk:

    def __init__(
        self,
        text
    ):
        self.page_content = text


chunks = [
    DummyChunk(
        "Agentic AI uses autonomous agents."
    ),
    DummyChunk(
        "Redis stores workflow state."
    ),
    DummyChunk(
        "ChromaDB stores vector embeddings."
    )
]


async def main():

    retriever = HybridRetriever(
        chunks
    )

    results = await retriever.retrieve(
        "What is Redis?"
    )

    print(results)


asyncio.run(main())