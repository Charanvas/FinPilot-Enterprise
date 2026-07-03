from app.tools.database.database_tool import DatabaseTool
from app.tools.ticket.ticket_tool import TicketTool
from app.tools.notification.notification_tool import NotificationTool

from app.schemas.audit_result_schema import AuditResultSchema

from app.core.logger import logger


class ActionAgent:
    """
    Executes business actions based on the audit result.
    """

    def __init__(self):

        self.database = DatabaseTool()

        self.ticket = TicketTool()

        self.notification = NotificationTool()

    def process(
        self,
        audit_result: AuditResultSchema,
        expected_amount: float,
    ) -> AuditResultSchema:

        logger.info("Action Agent started.")

        saved_invoice = self.database.save_invoice(
            invoice=audit_result.invoice,
            expected_amount=expected_amount,
            status=audit_result.action,
        )

        ticket_id = None

        if audit_result.action == "RAISE_TICKET":

            ticket = self.ticket.create_ticket(
                invoice_id=saved_invoice.id,
                description=audit_result.decision.reason,
            )

            ticket_id = ticket.id

        self.notification.send_notification(
            title="Invoice Audit Completed",
            message=f"{audit_result.invoice.invoice_number} → {audit_result.action}",
        )

        logger.info("Action Agent completed.")

        return audit_result.model_copy(
            update={
                "ticket_id": ticket_id
            }
        )