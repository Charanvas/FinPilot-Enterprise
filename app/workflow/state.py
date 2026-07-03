from typing import TypedDict

from app.schemas.invoice_schema import InvoiceSchema
from app.schemas.audit_result_schema import AuditResultSchema


class WorkflowState(TypedDict):
    """
    Shared state passed between LangGraph nodes.
    """

    file_path: str

    expected_amount: float

    invoice: InvoiceSchema | None

    audit_result: AuditResultSchema | None