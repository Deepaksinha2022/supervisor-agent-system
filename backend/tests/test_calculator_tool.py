import asyncio

from backend.app.tools.calculator_tool import (
    CalculatorTool
)


async def main():

    tool = CalculatorTool()

    result = await tool.execute(
        "10 + 20"
    )

    print(result)


asyncio.run(main())