from app.core.langsmith_config import *

from app.graphs.supervisor_graph import (
    planner_node,
    researcher_node,
    synthesizer_node
)

state = {
    "query": "What is Agentic AI?",
    "plan": [],
    "results": [],
    "final_answer": ""
}

state = planner_node(state)

state = researcher_node(state)

state = synthesizer_node(state)

print(state)