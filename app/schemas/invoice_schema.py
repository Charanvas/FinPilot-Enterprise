from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class InvoiceSchema(BaseModel):
    """
    Standard invoice object used across the application.
    """

    invoice_number: Optional[str] = Field(
        default=None,
        description="Unique invoice number"
    )

    vendor_name: Optional[str] = Field(
        default=None,
        description="Vendor or supplier name"
    )

    invoice_date: Optional[datetime] = Field(
        default=None,
        description="Invoice issue date"
    )

    invoice_total: Optional[float] = Field(
        default=None,
        description="Final invoice amount"
    )

    class Config:
        from_attributes = True