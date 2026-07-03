from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.database.models import Invoice

from app.core.logger import logger
from app.schemas.invoice_schema import InvoiceSchema


class DatabaseTool:
    """
    Tool responsible for all invoice database operations.
    """

    def __init__(self):

        self.db: Session = SessionLocal()

    def save_invoice(
        self,
        invoice: InvoiceSchema,
        expected_amount: float,
        status: str,
    ) -> Invoice:

        try:

            # Check if invoice already exists
            existing_invoice = self.get_invoice(invoice.invoice_number)

            if existing_invoice:
                logger.info("Invoice already exists in database.")
                return existing_invoice

            db_invoice = Invoice(
                invoice_number=invoice.invoice_number,
                vendor_name=invoice.vendor_name,
                invoice_date=invoice.invoice_date,
                expected_amount=expected_amount,
                actual_amount=invoice.invoice_total,
                status=status,
            )

            self.db.add(db_invoice)
            self.db.commit()
            self.db.refresh(db_invoice)

            logger.info("Invoice saved successfully.")

            return db_invoice

        except Exception as e:

            self.db.rollback()

            logger.error(e)

            raise

    def get_invoice(
        self,
        invoice_number: str,
    ) -> Invoice | None:

        return (
            self.db.query(Invoice)
            .filter(Invoice.invoice_number == invoice_number)
            .first()
        )

    def get_all_invoices(self):
        """
        Return all invoices ordered by newest first.
        """

        return (
            self.db.query(Invoice)
            .order_by(Invoice.created_at.desc())
            .all()
        )

    def delete_invoice(
        self,
        invoice_number: str,
    ) -> bool:

        invoice = self.get_invoice(invoice_number)

        if invoice:

            self.db.delete(invoice)
            self.db.commit()

            logger.info("Invoice deleted successfully.")

            return True

        logger.warning("Invoice not found.")

        return False

    def close(self):

        self.db.close()