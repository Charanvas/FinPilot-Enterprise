from app.tools.document.document_processor import DocumentProcessor
from app.tools.document.invoice_parser_tool import InvoiceParserTool
from app.tools.finance.calculator_tool import CalculatorTool
from app.tools.ai.gemini_tool import GeminiTool

from app.tools.database.database_tool import DatabaseTool
from app.tools.ticket.ticket_tool import TicketTool
from app.tools.notification.notification_tool import NotificationTool

from app.services.decision_engine import DecisionEngine

from app.schemas.audit_result_schema import AuditResultSchema

from app.core.logger import logger


class InvoiceAuditorAgent:
    """
    Main AI Agent responsible for auditing invoices.
    """

    def __init__(self):

        self.document_processor = DocumentProcessor()

        self.parser = InvoiceParserTool()

        self.calculator = CalculatorTool()

        self.gemini = GeminiTool()

        self.database = DatabaseTool()

        self.ticket = TicketTool()

        self.notification = NotificationTool()

        self.decision_engine = DecisionEngine()

    def audit(
        self,
        file_path: str,
        expected_amount: float,
    ):

        logger.info("Invoice auditing started.")

        # --------------------------------------------------
        # Step 1 : Extract text from document
        # --------------------------------------------------

        raw_text = self.document_processor.extract_text(file_path)

        # --------------------------------------------------
        # Step 2 : Parse invoice
        # --------------------------------------------------

        invoice = self.parser.extract(raw_text)

        # --------------------------------------------------
        # Step 3 : Calculate difference
        # --------------------------------------------------

        calculation = self.calculator.compare_amounts(
            expected_amount=expected_amount,
            actual_amount=invoice.invoice_total,
        )

        # --------------------------------------------------
        # Step 4 : AI Analysis
        # --------------------------------------------------

        prompt = f"""
Vendor: {invoice.vendor_name}

Invoice Number: {invoice.invoice_number}

Invoice Total: {invoice.invoice_total}

Expected Amount: {expected_amount}

Difference: {calculation["difference"]}
"""

        decision = self.gemini.analyze(prompt)

        # --------------------------------------------------
        # Step 5 : Business Decision
        # --------------------------------------------------

        business_action = self.decision_engine.decide(
            difference=calculation["difference"],
            ai_decision=decision,
        )

        # --------------------------------------------------
        # Step 6 : Save Invoice
        # --------------------------------------------------

        saved_invoice = self.database.save_invoice(
            invoice=invoice,
            expected_amount=expected_amount,
            status=business_action,
        )

        # --------------------------------------------------
        # Step 7 : Create Ticket (Only if required)
        # --------------------------------------------------

        ticket = None

        if business_action == "RAISE_TICKET":

            ticket = self.ticket.create_ticket(
                invoice_id=saved_invoice.id,
                description=decision.reason,
            )

        # --------------------------------------------------
        # Step 8 : Send Notification
        # --------------------------------------------------

        self.notification.send_notification(
            title="Invoice Audit Completed",
            message=f"{invoice.invoice_number} → {business_action}",
        )

        logger.info("Invoice auditing completed.")

        # --------------------------------------------------
        # Step 9 : Return Result
        # --------------------------------------------------

        return AuditResultSchema(
    invoice=invoice,
    calculation=calculation,
    decision=decision,
    action=business_action,
    ticket_id=ticket.id if ticket else None,
)