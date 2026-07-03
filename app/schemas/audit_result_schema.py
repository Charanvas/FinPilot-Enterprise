from typing import Dict, Optional

from pydantic import BaseModel

from app.schemas.invoice_schema import InvoiceSchema
from app.schemas.ai_decision_schema import AIDecisionSchema


class AuditResultSchema(BaseModel):
    """
    Final result returned by the Invoice Auditor Agent.
    """

    invoice: InvoiceSchema

    calculation: Dict

    decision: AIDecisionSchema

    action: str

    ticket_id: Optional[int] = None