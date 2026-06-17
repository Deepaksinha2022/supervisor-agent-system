from app.agents.retrieval_agent import RetrievalAgent

agent = RetrievalAgent()

collection = agent.get_collection("research_docs")

print(collection.name)