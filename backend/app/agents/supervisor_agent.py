from backend.app.agents.retrieval_agent import (
    RetrievalAgent
)

from backend.app.agents.synthesis_agent import (
    SynthesisAgent
)

from backend.app.agents.task_executor import (
    TaskExecutor
)

import asyncio

import time

class SupervisorAgent:

    def __init__(self, chunks=None):

        if chunks is not None:
            self.retrieval_agent = RetrievalAgent(
                chunks
            )

        self.synthesis_agent = SynthesisAgent()

        self.task_executor = TaskExecutor()

        self.agent_routes = {
        "Research": "retrieval_agent",
        "Compare": "compare_agent",
        "Summary": "synthesis_agent",
        }

    async def run(
        self,
        query
    ):

        retrieval_results = (
            await self.retrieval_agent.retrieve(
                query
            )
        )

        answer = (
            self.synthesis_agent.synthesize(
                query=query,
                web_results=[],
                retrieval_results=retrieval_results
            )
        )

        return answer

    async def execute_task(
        self,
        task_name: str
        ):

        route = None

        for key, value in self.agent_routes.items():

            if key in task_name:
                route = value
                break

        return await self.task_executor.execute(
        task_name,
        route
        )
    
    async def execute_plan(
        self,
        workflow_id: str,
        plan_manager
    ):

        while True:

            plan_manager.requeue_failed_tasks(
                workflow_id
            )


            ready_tasks = plan_manager.get_ready_tasks(
                workflow_id
            )

            if not ready_tasks:
                break
         

            await asyncio.gather(
                *[
                    self.execute_single_task(
                        workflow_id,
                        task,
                        plan_manager
                    )
                    for task in ready_tasks
                ]
            )

        if plan_manager.workflow_failed(
                workflow_id
            ):
            print(
                "\nWorkflow Status: FAILED\n"
            )
        if plan_manager.workflow_completed(
                workflow_id
            ):
            print(
                "\nWorkflow Status: COMPLETED\n"
            )
        summary = plan_manager.get_workflow_summary(
            workflow_id
        )

        print("\nWorkflow Summary:\n")
        print(summary)


        return plan_manager.get_plan(
            workflow_id
        )
    
    async def execute_single_task(
            self,
            workflow_id,
            task,
            plan_manager
        ):

       
        start_time = time.time()

        plan_manager.update_task_status(
            workflow_id,
            task["task_id"],
            "running"
        )

        result = await self.execute_task(
            task["task_name"]
        )

        execution_time = (
        time.time() - start_time
        )

        plan_manager.save_task_metric(
            workflow_id,
            task["task_id"],
            "execution_time",
            execution_time
        )
        
        if (
            result["needs_retry"]
            and task["retry_count"] < 3
        ):

            plan_manager.increment_retry_count(
                workflow_id,
                task["task_id"]
            )

            result["status"] = "retrying"

        plan_manager.save_task_result(
            workflow_id,
            task["task_id"],
            result
        )

        if result["approved"]:

            plan_manager.update_task_status(
                workflow_id,
                task["task_id"],
                "completed"
                )

        else:

            plan_manager.update_task_status(
                workflow_id,
                task["task_id"],
                "failed"
        )