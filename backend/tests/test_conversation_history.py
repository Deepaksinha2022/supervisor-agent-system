from app.state.conversation_history import (
    add_message,
    get_history,
    get_recent_history
)

session_id = "test_session"

add_message(
    session_id,
    "user",
    "What is Agentic AI?"
)

add_message(
    session_id,
    "assistant",
    "Agentic AI uses autonomous agents."
)

print(get_history(session_id))

print(
    get_recent_history(
        session_id,
        limit=1
    )
)