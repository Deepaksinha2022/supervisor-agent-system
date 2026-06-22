from backend.app.agents.base_agent import (
    BaseAgent
)


class SummaryAgent(BaseAgent):

    @property
    def capabilities(self):
        return [
            "summary",
            "summarize",
            "generate"
        ]

    async def execute(
        self,
        task_name: str
    ):

        return (
            f"Summary completed: "
            f"{task_name}"
        )