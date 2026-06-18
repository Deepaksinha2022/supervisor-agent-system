from typing import TypedDict

from langgraph.graph import StateGraph, END

from langsmith import traceable

from app.utils.state_manager import save_state

class AgentState(TypedDict):
    session_id: str
    query: str
    plan: list[str]
    results: list[str]
    final_answer: str

@traceable
def planner_node(state: AgentState):
    query = state["query"]

    save_state(
    state["session_id"],
    {
        "query": state["query"],
        "step": "planning",
        "plan": [f"Research: {query}", "Summarize findings"]
    }
)

    return {"plan": [f"Research: {query}", "Summarize findings"]}

@traceable
def researcher_node(state: AgentState):
    plan = state["plan"]

    save_state(
    state["session_id"],
    {
        "query": state["query"],
        "step": "researching",
        "plan": state["plan"],
        "results": [f"Completed: {task}" for task in plan]
    }
)
    return {
        "results": [f"Completed: {task}" for task in plan]
    }

@traceable
def synthesizer_node(state: AgentState):
    results = state["results"]

    save_state(
    state["session_id"],
    {
        "query": state["query"],
        "step": "completed",
        "plan": state["plan"],
        "results": state["results"],
        "final_answer": "\n".join(results)
    }
)
    return {
        "final_answer": "\n".join(results)
    }

graph = StateGraph(AgentState)
graph.add_node("planner", planner_node)
graph.add_node("researcher", researcher_node)
graph.add_node("synthesizer", synthesizer_node)

graph.set_entry_point("planner")

graph.add_edge("planner", "researcher")
graph.add_edge("researcher", "synthesizer")
graph.add_edge("synthesizer", END)

app = graph.compile()

result = app.invoke(
    {
        "session_id": "session_1",
        "query": "What is Agentic AI?",
        "plan": [],
        "results": [],
        "final_answer": ""
    }
)

print(result)