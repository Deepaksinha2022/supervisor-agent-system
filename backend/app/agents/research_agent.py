from backend.app.agents.base_agent import (
    BaseAgent
)


class ResearchAgent(BaseAgent):


    def __init__(
            self,
            tool_executor=None
        ):
        self.tool_executor = tool_executor

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

        if self.tool_executor:

            tool_result = (
                await self.tool_executor.auto_execute(
                    "math calculation",
                    "10 + 20"
                    )
                )

            return (
                f"Research completed: "
                f"{task_name} | "
                f"Tool Result: {tool_result}"
                )