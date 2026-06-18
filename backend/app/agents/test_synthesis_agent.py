from app.agents.synthesis_agent import SynthesisAgent

agent = SynthesisAgent()

result = agent.synthesize(
    web_results=["result1"],
    retrieval_results=["result2"]
)

print(result)