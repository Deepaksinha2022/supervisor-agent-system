from backend.app.tools.tool_router import (
    ToolRouter
)


class ToolExecutor:

    def __init__(
        self,
        registry
        ):

        self.registry = registry

        self.router = ToolRouter(
            registry
        )

    async def execute(
        self,
        tool_name,
        *args,
        **kwargs
    ):

        tool = self.registry.get(
            tool_name
        )

        if not tool:
            raise ValueError(
                f"Tool not found: {tool_name}"
            )

        return await tool.execute(
            *args,
            **kwargs
        )
    
    async def auto_execute(
            self,
            task,
            *args,
            **kwargs
        ):

        tool = self.router.route(
            task
        )

        if not tool:
            return None

        return await tool.execute(
            *args,
            **kwargs
        )