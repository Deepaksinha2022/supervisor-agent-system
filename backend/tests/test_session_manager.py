from app.state.session_manager import (
    create_session_id,
    save_session,
    get_session,
    add_workflow_to_session
)

from app.state.workflow_state import create_workflow_id

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

print(get_session(session_id))