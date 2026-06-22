import uuid

from app.core.redis_client import redis_client

import json

def save_session(session_id: str, session_data: dict):

    redis_client.set(
        f"session:{session_id}",
        json.dumps(session_data)
    )

def get_session(session_id: str):

    data = redis_client.get(f"session:{session_id}")

    if not data:
        return None

    return json.loads(data)

def create_session_id():

    return str(uuid.uuid4())

def add_workflow_to_session(
    session_id: str,
    workflow_id: str
):
    session = get_session(session_id)

    if not session:
        return

    session["workflow_ids"].append(workflow_id)

    save_session(session_id, session)