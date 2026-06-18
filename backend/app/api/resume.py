from fastapi import APIRouter

from app.utils.state_manager import resume_state

router = APIRouter()


@router.get("/resume/{session_id}")
def resume(session_id: str):

    state = resume_state(session_id)

    if not state:
        return {"message": "Session not found"}

    return state