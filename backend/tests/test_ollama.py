from app.llm.ollama_client import llm

response = llm.invoke(
    "What is Redis?"
)

print(response)