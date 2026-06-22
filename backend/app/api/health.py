from fastapi import APIRouter
from app.core.redis_client import redis_client

router = APIRouter()

@router.get("/health/redis")
def redis_health():
    try:
        redis_client.ping()
        return {"status": "healthy"}
    except Exception as e:
        return {"status": "unhealthy", "error": str(e)}