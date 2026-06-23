from backend.app.tools.tool_registry import (
    ToolRegistry
)

from backend.app.tools.calculator_tool import (
    CalculatorTool
)

registry = ToolRegistry()

registry.register(
    "calculator_tool",
    CalculatorTool()
)
tool = registry.get(
    "calculator_tool"
)

print(
    tool.capabilities
)

print(tool.tool_name)

# print(
#     registry.list_tools()
# )