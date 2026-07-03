from app.agents.document_agent import DocumentAgent
from app.agents.finance_agent import FinanceAgent
from app.agents.action_agent import ActionAgent

document_agent = DocumentAgent()
finance_agent = FinanceAgent()
action_agent = ActionAgent()

invoice = document_agent.process(
    "uploads/invoice.pdf"
)

audit = finance_agent.process(
    invoice,
    expected_amount=400,
)

result = action_agent.process(
    audit_result=audit,
    expected_amount=400,
)

print(result.model_dump())