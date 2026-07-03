from app.agents.document_agent import DocumentAgent

agent = DocumentAgent()

invoice = agent.process(
    "uploads/invoice.pdf"
)

print(invoice.model_dump())