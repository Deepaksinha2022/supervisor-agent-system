from app.core.langsmith_config import *

from app.agents.web_search_agent import WebSearchAgent
from app.agents.retrieval_agent import RetrievalAgent
from app.agents.synthesis_agent import SynthesisAgent


web_agent = WebSearchAgent()

web_agent.search("What is Agentic AI?")

retrieval_agent = RetrievalAgent()

retrieval_agent.get_collection("research_docs")

synthesis_agent = SynthesisAgent()

synthesis_agent.synthesize(
    web_results=["AI article"],
    retrieval_results=["Internal document"]
)

print("All agents executed")