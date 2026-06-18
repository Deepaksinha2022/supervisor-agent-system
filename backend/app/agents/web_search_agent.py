from tavily import TavilyClient

import os

from langsmith import traceable

from dotenv import load_dotenv

from app.prompts.prompt_logger import log_prompt_version

load_dotenv()

class WebSearchAgent:

    def __init__(self):
        self.client = TavilyClient(
        api_key=os.getenv("TAVILY_API_KEY")
    )

    @traceable

    def search(self, query: str):

        log_prompt_version("web_search_agent")

        response = self.client.search(
            query=query,
            max_results=5
        )

        return response