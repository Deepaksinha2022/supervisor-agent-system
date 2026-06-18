import json

from app.utils.redis_client import redis_client


def save_state(session_id: str, state: dict):

    redis_client.set(
        session_id,
        json.dumps(state),
        ex=3600
    )


def load_state(session_id: str):

    data = redis_client.get(session_id)

    if not data:
        return None

    return json.loads(data)

def delete_state(session_id: str):
    redis_client.delete(session_id)

def resume_state(session_id: str):
    return load_state(session_id)

def is_completed(session_id: str):

    state = load_state(session_id)

    if not state:
        return False

    return state.get("step") == "completed"