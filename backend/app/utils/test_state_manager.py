from app.utils.state_manager import (
    save_state,
    load_state,
    delete_state
)

from app.models.research_state import ResearchState

state = ResearchState(
    query="What is Agentic AI?",
    step="researching",
    results=[]
)

save_state("session_1", state.model_dump())

print(load_state("session_1"))

delete_state("session_1")

print(load_state("session_1"))