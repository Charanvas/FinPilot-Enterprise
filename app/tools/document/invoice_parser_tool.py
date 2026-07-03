import re
from typing import Optional
from datetime import datetime
from app.core.logger import logger
from app.schemas.invoice_schema import InvoiceSchema


class InvoiceParserTool:
    """
    Extract important invoice fields from raw invoice text.
    """

    def __init__(self):
        pass

    def extract(self, text: str) -> InvoiceSchema:
        """
        Extract invoice information from raw text.

        Args:
            text (str): Raw text extracted from invoice.

        Returns:
            InvoiceSchema: Structured invoice data.
        """

        try:

            invoice_number = self._find(
                r"Invoice No:\s*([A-Za-z0-9]+)",
                text
            )

            vendor_name = self._find(
                r"Restaurant Name:\s*(.+)",
                text
            )

            invoice_date_str = self._find(
            r"Date of Invoice:\s*(\d{2}-\d{2}-\d{4})",
            text
        )
            invoice_date = None

            if invoice_date_str:
                invoice_date = (
                datetime.strptime(invoice_date_str, "%d-%m-%Y")
                if invoice_date_str
                else None
            )

            invoice_total = self._find(
                r"Invoice Total\s*([\d.]+)",
                text
            )

            logger.info("Invoice parsed successfully.")

            return InvoiceSchema(
                invoice_number=invoice_number,
                vendor_name=vendor_name,
                invoice_date=invoice_date,
                invoice_total=float(invoice_total)
                if invoice_total
                else None,
            )

        except Exception as e:

            logger.error(f"Invoice parsing failed: {e}")

            return InvoiceSchema()

    def _find(
        self,
        pattern: str,
        text: str
    ) -> Optional[str]:

        match = re.search(pattern, text)

        if match:
            return match.group(1).strip()

        return None