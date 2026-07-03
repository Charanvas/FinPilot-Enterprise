from sqlalchemy.orm import Session

from app.core.database import SessionLocal
from app.database.models import Ticket
from app.core.logger import logger


class TicketTool:
    """
    Creates manual review tickets.
    """

    def __init__(self):
        self.db: Session = SessionLocal()

    def create_ticket(
        self,
        invoice_id: int,
        description: str,
        priority: str = "HIGH",
    ) -> Ticket:

        try:
            ticket = Ticket(
                invoice_id=invoice_id,
                priority=priority,
                description=description,
                status="OPEN",
            )

            self.db.add(ticket)
            self.db.commit()
            self.db.refresh(ticket)

            logger.info(f"Ticket #{ticket.id} created.")

            return ticket

        except Exception as e:
            self.db.rollback()
            logger.error(e)
            raise

    def close(self):
        self.db.close()