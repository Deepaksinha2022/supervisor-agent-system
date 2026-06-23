import asyncio

from backend.app.tools.tool_registry import (
    ToolRegistry
)

from backend.app.tools.tool_executor import (
    ToolExecutor
)

from backend.app.tools.calculator_tool import (
    CalculatorTool
)


async def main():

    registry = ToolRegistry()

    registry.register(
        "calculator_tool",
        CalculatorTool()
    )

    executor = ToolExecutor(
        registry
    )

    result = await executor.execute(
        "calculator_tool",
        "10 + 20"
    )

    print(result)


asyncio.run(main())