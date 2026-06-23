class ToolRouter:

    def __init__(
        self,
        registry
    ):
        self.registry = registry

    def route(
        self,
        task
    ):

        task = task.lower()

        for tool in self.registry.tools.values():

            for capability in tool.capabilities:

                if capability in task:
                    return tool

        return None