from app.tools.finance.calculator_tool import CalculatorTool
from app.tools.ai.gemini_tool import GeminiTool
from app.services.decision_engine import DecisionEngine

from app.schemas.invoice_schema import InvoiceSchema
from app.schemas.audit_result_schema import AuditResultSchema

from app.core.logger import logger


class FinanceAgent:
    """
    Responsible for financial validation and AI reasoning.
    """

    def __init__(self):

        self.calculator = CalculatorTool()

        self.gemini = GeminiTool()

        self.decision_engine = DecisionEngine()

    def process(
        self,
        invoice: InvoiceSchema,
        expected_amount: float,
    ) -> AuditResultSchema:

        logger.info("Finance Agent started.")

        calculation = self.calculator.compare_amounts(
            expected_amount=expected_amount,
            actual_amount=invoice.invoice_total,
        )

        prompt = f"""
Vendor: {invoice.vendor_name}

Invoice Number: {invoice.invoice_number}

Invoice Total: {invoice.invoice_total}

Expected Amount: {expected_amount}

Difference: {calculation["difference"]}
"""

        decision = self.gemini.analyze(prompt)

        action = self.decision_engine.decide(
            difference=calculation["difference"],
            ai_decision=decision,
        )

        logger.info("Finance Agent completed.")

        return AuditResultSchema(
            invoice=invoice,
            calculation=calculation,
            decision=decision,
            action=action,
            ticket_id=None,
        )