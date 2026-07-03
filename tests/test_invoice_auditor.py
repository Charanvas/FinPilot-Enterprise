from app.agents.invoice_auditor_agent import InvoiceAuditorAgent

agent = InvoiceAuditorAgent()

result = agent.audit(
    file_path="uploads/invoice.pdf",
    expected_amount=400,
)

print(result.model_dump())