from langsmith import traceable

from backend.app.llm.ollama_client import llm


class SynthesisAgent:

    @traceable
    def synthesize(
        self,
        query,
        web_results,
        retrieval_results
    ):

        prompt = f"""
Question:
{query}

Web Results:
{web_results}

Retrieved Documents:
{retrieval_results}

Answer the question using the available information.
"""

        response = llm.invoke(
            prompt
        )

        return response