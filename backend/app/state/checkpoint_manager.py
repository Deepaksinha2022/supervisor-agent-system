from app.core.redis_client import redis_client
import json


def save_checkpoint(
    workflow_id: str,
    checkpoint_data: dict
):
    redis_client.set(
        f"checkpoint:{workflow_id}",
        json.dumps(checkpoint_data)
    )


def get_checkpoint(workflow_id: str):
    data = redis_client.get(
        f"checkpoint:{workflow_id}"
    )

    if not data:
        return None

    return json.loads(data)

def update_checkpoint(
    workflow_id: str,
    completed_agent: str,
    next_agent: str,
    output:dict
):
    checkpoint = get_checkpoint(workflow_id)

    if not checkpoint:
        checkpoint = {
        "completed_agents": [],
        "agent_outputs": {}
    }
        
    if "agent_outputs" not in checkpoint:
        checkpoint["agent_outputs"] = {}

    checkpoint["completed_agents"].append(
        completed_agent
    )

    checkpoint["agent_outputs"][completed_agent] = output

    checkpoint["next_agent"] = next_agent

    save_checkpoint(
        workflow_id,
        checkpoint
    )