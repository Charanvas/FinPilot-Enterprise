from app.agents.document_agent import DocumentAgent
from app.agents.finance_agent import FinanceAgent
from app.agents.action_agent import ActionAgent

from app.schemas.audit_result_schema import AuditResultSchema

from app.core.logger import logger


class SupervisorAgent:
    """
    Coordinates all specialized agents.
    """

    def __init__(self):

        self.document_agent = DocumentAgent()

        self.finance_agent = FinanceAgent()

        self.action_agent = ActionAgent()

    def process(
        self,
        file_path: str,
        expected_amount: float,
    ) -> AuditResultSchema:

        logger.info("Supervisor Agent started.")

        # Step 1
        invoice = self.document_agent.process(file_path)

        # Step 2
        audit_result = self.finance_agent.process(
            invoice=invoice,
            expected_amount=expected_amount,
        )

        # Step 3
        final_result = self.action_agent.process(
            audit_result=audit_result,
            expected_amount=expected_amount,
        )

        logger.info("Supervisor Agent completed.")

        return final_result