import os

from app.core.langsmith_config import *

from langsmith import traceable

print(os.getenv("LANGCHAIN_API_KEY"))
print(os.getenv("LANGCHAIN_TRACING_V2"))
print(os.getenv("LANGCHAIN_PROJECT"))

@traceable
def test_function():

    return "LangSmith Working"


print(test_function())