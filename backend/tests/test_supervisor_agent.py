import asyncio

from app.agents.supervisor_agent import (
    SupervisorAgent
)


class DummyChunk:

    def __init__(self, text):

        self.page_content = text


chunks = [
    DummyChunk(
        "Redis is an in-memory key-value database used for caching, session storage and workflow state management."
    ),
    DummyChunk(
        "Redis provides very fast read and write operations because data is stored in memory."
    ),
    DummyChunk(
        "Redis supports strings, hashes, lists, sets and sorted sets."
    )
]


async def main():

    supervisor = SupervisorAgent(
        chunks
    )

    response = await supervisor.run(
        "What is Redis?"
    )

    print(response)


asyncio.run(main())