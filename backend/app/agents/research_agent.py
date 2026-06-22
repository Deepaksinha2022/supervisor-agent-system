from backend.app.agents.base_agent import (
    BaseAgent
)


class ResearchAgent(BaseAgent):

    @property
    def capabilities(self):
        return [
            "research",
            "retrieve",
            "search"
        ]

    async def execute(
        self,
        task_name: str
    ):

        return (
            f"Research completed: "
            f"{task_name}"
        )