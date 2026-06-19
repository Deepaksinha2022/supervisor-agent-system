from fastapi import APIRouter

from sse_starlette.sse import EventSourceResponse

import asyncio

from app.graphs.supervisor_graph import app

import uuid

router = APIRouter()

async def event_generator():

    session_id = str(uuid.uuid4())

    yield {"data": "Supervisor: Starting"}

    result = app.invoke(
        {
            "session_id": session_id,
            "query": "What is Agentic AI?",
            "plan": [],
            "results": [],
            "final_answer": ""
        }
    )

    yield {"data": "Workflow Complete"}

    yield {
        "data": result["final_answer"]
    }


@router.get("/stream")
async def stream():

    return EventSourceResponse(
        event_generator()
    )