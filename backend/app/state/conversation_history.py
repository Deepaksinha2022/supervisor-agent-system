from app.core.redis_client import redis_client

import json

from datetime import datetime

def add_message(
    session_id: str,
    role: str,
    content: str
):
    key = f"history:{session_id}"

    message = {
        "role": role,
        "content": content,
        "timestamp": datetime.utcnow().isoformat()
    }

    redis_client.rpush(
        key,
        json.dumps(message)
    )

def get_history(session_id: str):
    key = f"history:{session_id}"

    messages = redis_client.lrange(
        key,
        0,
        -1
    )

    return [
        json.loads(msg)
        for msg in messages
    ]

def get_recent_history(
    session_id: str,
    limit: int = 10
):
    key = f"history:{session_id}"

    messages = redis_client.lrange(
        key,
        -limit,
        -1
    )

    return [
        json.loads(msg)
        for msg in messages
    ]