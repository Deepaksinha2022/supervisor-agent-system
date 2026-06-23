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

from backend.app.tools.tool_registry import (
    ToolRegistry
)

from backend.app.tools.tool_executor import (
    ToolExecutor
)

from backend.app.tools.calculator_tool import (
    CalculatorTool
)

from backend.app.models.model_registry import (
    ModelRegistry
)

from backend.app.models.model_router import (
    ModelRouter
)

from backend.app.metrics.cost_tracker import (
    CostTracker
)

class TaskExecutor:

    def __init__(self):

            self.registry = AgentRegistry()

            tool_registry = ToolRegistry()

            tool_registry.register(
                "calculator_tool",
                CalculatorTool()
            )

            self.tool_executor = ToolExecutor(
                tool_registry
            )

            self.model_registry = ModelRegistry()

            self.model_registry.register(
                "small_model",
                {
                    "name": "TinyLLM",
                    "cost_per_call": 0.0001,
                    "latency_ms": 100
                }
            )

            self.model_registry.register(
                "medium_model",
                {
                    "name": "Mistral",
                    "cost_per_call": 0.001,
                    "latency_ms": 500
                }
            )

            self.model_registry.register(
                "large_model",
                {
                    "name": "Llama",
                    "cost_per_call": 0.01,
                    "latency_ms": 2000
                }
            )

            self.model_router = ModelRouter(
                self.model_registry
            )

            self.cost_tracker = CostTracker()

            self.research_agent = ResearchAgent(
                self.tool_executor
            )

            self.compare_agent = CompareAgent()

            self.summary_agent = SummaryAgent()

            self.reflection_agent = ReflectionAgent()

            self.critic_agent = CriticAgent()

            self.registry.register(
                "research_agent",
                self.research_agent
            )

            self.registry.register(
                "compare_agent",
                self.compare_agent
            )

            self.registry.register(
                "summary_agent",
                self.summary_agent
            )

            self.registry.register(
                "reflection_agent",
                self.reflection_agent
            )

            self.registry.register(
                "critic_agent",
                self.critic_agent
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

        model = self.model_router.route(
            task_name
        )

        self.cost_tracker.track(
            task_name,
            model
        )


        print(
            f"\nModel Selected: "
            f"{model['name']}"
        )

        print(
            f"Cost: "
            f"{model['cost_per_call']}"
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
                "needs_retry": critic["score"] < 0.80,
                "requires_human_approval": False
            }

        return (
            f"Executed by {route}: "
            f"{task_name}"
        )