class DynamicAgentRouter:

    def __init__(
        self,
        registry
    ):
        self.registry = registry

    def route(
        self,
        task_name: str
    ):

        task_lower = task_name.lower()

        for agent in self.registry.agents.values():

            for capability in agent.capabilities:

                if capability in task_lower:
                    return agent

        return None