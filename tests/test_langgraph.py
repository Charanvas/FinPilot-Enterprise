from app.workflow.graph import graph

result = graph.invoke(
    {
        "file_path": "uploads/invoice.pdf",
        "expected_amount": 400,
        "invoice": None,
        "audit_result": None,
    }
)

print(result["audit_result"].model_dump())