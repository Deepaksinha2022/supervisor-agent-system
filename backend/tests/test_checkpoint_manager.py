from app.state.workflow_state import create_workflow_id
from app.state.checkpoint_manager import (
    save_checkpoint,
    get_checkpoint,
    update_checkpoint
)

workflow_id = create_workflow_id()

checkpoint = {
    "completed_agents": [
        "search_agent",
        "retrieval_agent"
    ],
    "next_agent": "synthesis_agent"
}

save_checkpoint(
    workflow_id,
    checkpoint
)

print(
    get_checkpoint(
        workflow_id
    )
)

update_checkpoint(
    workflow_id,
    "search_agent",
    "retrieval_agent",
    {
        "sources": [
            "source1",
            "source2"
        ]
    }
)

update_checkpoint(
    workflow_id,
    "retrieval_agent",
    "synthesis_agent",
    {
        "documents": [
            "doc1",
            "doc2"
        ]
    }
)

print(
    get_checkpoint(
        workflow_id
    )
)