import asyncio

from app.agents.retrieval_agent import (
    RetrievalAgent
)

from app.agents.synthesis_agent import (
    SynthesisAgent
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

    retrieval_agent = RetrievalAgent(
        chunks
    )

    synthesis_agent = SynthesisAgent()

    retrieved_docs = await retrieval_agent.retrieve(
        "What is Redis?"
    )

    response = synthesis_agent.synthesize(
        query="What is Redis?",
        web_results=[],
        retrieval_results=retrieved_docs
    )

    print(response)


asyncio.run(main())