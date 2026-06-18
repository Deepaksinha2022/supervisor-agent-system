from tavily import TavilyClient

import os

from langsmith import traceable

from dotenv import load_dotenv

from app.prompts.prompt_logger import log_prompt_version

from app.prompts.ab_experiment import get_prompt_variant

load_dotenv()

class WebSearchAgent:

    def __init__(self):
        self.client = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
    )

    @traceable

    def search(self, query: str):
        
        variant = get_prompt_variant()

        log_prompt_version(
    "web_search_agent",
    variant
)

        response = self.client.search(
            query=query,
            max_results=5
        )

        return response