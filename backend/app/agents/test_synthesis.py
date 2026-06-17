from app.agents.synthesis_agent import SynthesisAgent

agent = SynthesisAgent()

result = agent.synthesize(
    web_results=["AI article", "Research paper"],
    retrieval_results=["Internal document"]
)

print(result)