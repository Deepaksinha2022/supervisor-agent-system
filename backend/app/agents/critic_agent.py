from backend.app.agents.base_agent import (
    BaseAgent
)


class CriticAgent(BaseAgent):

    @property
    def capabilities(self):
        return [
            "critic",
            "critique",
            "review"
        ]

    async def execute(
        self,
        task_result: str
    ):

        return {
        "feedback": (
        f"Critic completed: "
        f"{task_result}"
    ),
        "score": 0.95
    }