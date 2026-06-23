from backend.app.tools.tool_registry import (
    ToolRegistry
)

from backend.app.tools.tool_router import (
    ToolRouter
)

from backend.app.tools.calculator_tool import (
    CalculatorTool
)


registry = ToolRegistry()

registry.register(
    "calculator_tool",
    CalculatorTool()
)

router = ToolRouter(
    registry
)

tool = router.route(
    "math operation"
)

print(
    tool.tool_name
)