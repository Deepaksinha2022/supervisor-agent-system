from langsmith import traceable

class SynthesisAgent:

    @traceable
    def synthesize(
        self,
        web_results,
        retrieval_results
    ):

        return {
            "web_results": web_results,
            "retrieval_results": retrieval_results
        }