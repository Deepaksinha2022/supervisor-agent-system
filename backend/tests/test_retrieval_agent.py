import asyncio

from app.agents.retrieval_agent import (
    RetrievalAgent
)


class DummyChunk:

    def __init__(self, text):

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

    agent = RetrievalAgent(
        chunks
    )

    results = await agent.retrieve(
        "What is Redis?"
    )

    print(results)


asyncio.run(main())