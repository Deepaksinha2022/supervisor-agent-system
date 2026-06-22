from backend.app.agents.base_agent import (
    BaseAgent
)


class ReflectionAgent(BaseAgent):

    @property
    def capabilities(self):
        return [
            "reflection",
            "review"
        ]

    async def execute(
        self,
        task_result: str
    ):

        return (
            f"Reflection completed: "
            f"{task_result}"
        )