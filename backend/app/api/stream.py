from fastapi import APIRouter
from sse_starlette.sse import EventSourceResponse
import asyncio

router = APIRouter()

async def event_generator():

    agents = [
        "Supervisor: Planning",
        "Web Agent: Searching",
        "Retrieval Agent: Fetching documents",
        "Synthesis Agent: Generating answer"
    ]

    for agent in agents:

        yield {"data": agent}

        await asyncio.sleep(1)

    yield {"data": "Workflow Complete"}


@router.get("/stream")
async def stream():

    return EventSourceResponse(
        event_generator()
    )