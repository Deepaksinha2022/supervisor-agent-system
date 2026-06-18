from typing import List
from pydantic import BaseModel


class ResearchState(BaseModel):
    query: str
    step: str
    results: List[str]