from backend.app.tools.base_tool import (
    BaseTool
)


class CalculatorTool(BaseTool):

    async def execute(
        self,
        expression: str
    ):

        return eval(
            expression
        )
    
    @property
    def capabilities(
        self
    ):
        return [
            "math",
            "calculation",
            "arithmetic"
        ]