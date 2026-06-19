from langsmith import traceable

from langsmith import traceable

from app.prompts.prompt_logger import log_prompt_version

from app.prompts.ab_experiment import get_prompt_variant

from app.prompts.prompt_logger import log_prompt_version

class SynthesisAgent:

    @traceable
    def synthesize(
        self,
        web_results,
        retrieval_results
    ):
        variant = get_prompt_variant()

        log_prompt_version(
    "synthesis_agent",
    variant
)
        
        return {
            "web_results": web_results,
            "retrieval_results": retrieval_results
        }