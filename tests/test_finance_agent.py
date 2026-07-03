from app.agents.document_agent import DocumentAgent
from app.agents.finance_agent import FinanceAgent

document_agent = DocumentAgent()
finance_agent = FinanceAgent()

invoice = document_agent.process(
    "uploads/invoice.pdf"
)

result = finance_agent.process(
    invoice=invoice,
    expected_amount=400,
)

print(result.model_dump())