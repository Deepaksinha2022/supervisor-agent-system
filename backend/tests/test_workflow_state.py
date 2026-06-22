from app.state.workflow_state import (
    create_workflow,
    get_workflow_state,
    pause_workflow,
    resume_workflow
)

from app.state.session_manager import (
    get_session
)

# Create Session + Workflow
session_id, workflow_id = create_workflow()

print("Session ID:")
print(session_id)

print("\nWorkflow ID:")
print(workflow_id)


# Verify Session
print("\nSession Data:")
print(
    get_session(
        session_id
    )
)

# Verify Workflow Before Pause
print("\nWorkflow Before Pause:")
print(
    get_workflow_state(
        workflow_id
    )
)


# Pause Workflow
pause_workflow(
    workflow_id
)


# Verify Workflow After Pause
print("\nWorkflow After Pause:")
print(
    get_workflow_state(
        workflow_id
    )
)

resume_workflow(
    workflow_id
)

print("\nWorkflow After Resume:")

print(
    get_workflow_state(
        workflow_id
    )
)