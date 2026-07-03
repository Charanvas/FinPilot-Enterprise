from app.agents.document_agent import DocumentAgent
from app.agents.finance_agent import FinanceAgent
from app.agents.action_agent import ActionAgent

from app.workflow.state import WorkflowState


document_agent = DocumentAgent()
finance_agent = FinanceAgent()
action_agent = ActionAgent()


def document_node(state: WorkflowState):

    invoice = document_agent.process(
        state["file_path"]
    )

    state["invoice"] = invoice

    return state


def finance_node(state: WorkflowState):

    audit = finance_agent.process(
        invoice=state["invoice"],
        expected_amount=state["expected_amount"],
    )

    state["audit_result"] = audit

    return state


def action_node(state: WorkflowState):

    audit = action_agent.process(
        audit_result=state["audit_result"],
        expected_amount=state["expected_amount"],
    )

    state["audit_result"] = audit

    return state