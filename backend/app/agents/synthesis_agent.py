from langsmith import traceable

from app.prompts.prompt_logger import log_prompt_version

class SynthesisAgent:

    @traceable
    def synthesize(
        self,
        web_results,
        retrieval_results
    ):
        log_prompt_version("synthesis_agent")
        
        return {
            "web_results": web_results,
            "retrieval_results": retrieval_results
        }