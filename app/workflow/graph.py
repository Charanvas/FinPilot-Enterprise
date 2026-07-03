from langgraph.graph import StateGraph, END

from app.workflow.state import WorkflowState
from app.workflow.nodes import (
    document_node,
    finance_node,
    action_node,
)

workflow = StateGraph(WorkflowState)

workflow.add_node("document", document_node)
workflow.add_node("finance", finance_node)
workflow.add_node("action", action_node)

workflow.set_entry_point("document")

workflow.add_edge("document", "finance")
workflow.add_edge("finance", "action")
workflow.add_edge("action", END)

graph = workflow.compile()