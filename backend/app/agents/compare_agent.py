from backend.app.agents.base_agent import (
    BaseAgent
)

class CompareAgent(BaseAgent):

    @property
    def capabilities(self):
        return [
            "compare",
            "comparison",
            "analysis"
        ]

    async def execute(
        self,
        task_name: str
    ):

        return (
            f"Comparison completed: "
            f"{task_name}"
        )