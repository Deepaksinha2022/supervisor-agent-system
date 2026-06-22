from backend.app.agents.compare_agent import (
    CompareAgent
)

from backend.app.agents.agent_registry import (
    AgentRegistry
)

from backend.app.agents.dynamic_agent_router import (
    DynamicAgentRouter
)

from backend.app.agents.research_agent import (
    ResearchAgent
)

from backend.app.agents.summary_agent import (
    SummaryAgent
)

from backend.app.agents.reflection_agent import (
    ReflectionAgent
)

from backend.app.agents.critic_agent import (
    CriticAgent
)

class TaskExecutor:

    def __init__(self):

        self.compare_agent = CompareAgent()

        self.registry = AgentRegistry()

        self.research_agent = ResearchAgent()

        self.summary_agent = SummaryAgent()

        self.reflection_agent = ReflectionAgent()

        self.critic_agent = CriticAgent()

        self.registry.register(
            "critic_agent",
            self.critic_agent
        )

        self.registry.register(
            "compare_agent",
            self.compare_agent
        )

        self.registry.register(
            "research_agent",
            self.research_agent
        )

        self.registry.register(
             "summary_agent",
                self.summary_agent
        )

        self.registry.register(
            "reflection_agent",
            self.reflection_agent
        )

        self.router = DynamicAgentRouter(
        self.registry
        )

    async def execute(
        self,
        task_name: str,
        route: str
    ):

        agent = self.router.route(
            task_name
        )

        if agent:

            result = await agent.execute(
                    task_name
            )

            reflection = await self.reflection_agent.execute(
                result
            )

            critic = await self.critic_agent.execute(
                reflection
            )

            return {
                "agent": agent.agent_name,
                "result": result,
                "reflection": reflection,
                "critic":critic,
                "approved":critic["score"]>=0.80,
                "needs_retry": critic["score"] < 0.80
            }

        return (
            f"Executed by {route}: "
            f"{task_name}"
        )