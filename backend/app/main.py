from fastapi import FastAPI

from app.api.stream import router as stream_router

from app.core.langsmith_config import *

app = FastAPI()

app.include_router(stream_router)

from app.api.resume import router as resume_router

app.include_router(resume_router)

@app.get("/")
def health():
    return {"status": "healthy"}

