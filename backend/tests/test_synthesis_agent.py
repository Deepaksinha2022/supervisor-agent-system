from app.agents.synthesis_agent import (
    SynthesisAgent
)

agent = SynthesisAgent()

response = agent.synthesize(
    query="What is Redis?",
    web_results=[],
    retrieval_results=[
        "Redis stores workflow state."
    ]
)

print(response)