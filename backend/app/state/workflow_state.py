from app.core.redis_client import redis_client

import json

from datetime import datetime

import uuid

from app.state.session_manager import (
    create_session_id,
    save_session,
    add_workflow_to_session
)

def create_workflow_id():
    return str(uuid.uuid4())

def save_workflow_state(workflow_id: str, state: dict):

    state["updated_at"] = datetime.utcnow().isoformat()

    redis_client.set(
        f"workflow:{workflow_id}",
        json.dumps(state)
    )
    
def get_workflow_state(workflow_id: str):

    data = redis_client.get(f"workflow:{workflow_id}")

    if not data:
        return None

    return json.loads(data)

def update_workflow_status(workflow_id: str, status: str):

    state = get_workflow_state(workflow_id)

    if not state:
        return

    state["status"] = status

    save_workflow_state(workflow_id, state)

def create_workflow():

    session_id = create_session_id()

    session = {
        "session_id": session_id,
        "workflow_ids": []
    }

    save_session(session_id, session)

    workflow_id = create_workflow_id()

    add_workflow_to_session(
        session_id,
        workflow_id
    )

    return session_id, workflow_id

def pause_workflow(workflow_id: str):
    update_workflow_status(
        workflow_id,
        "paused"
    )

def resume_workflow(workflow_id: str):
    update_workflow_status(
        workflow_id,
        "running"
    )