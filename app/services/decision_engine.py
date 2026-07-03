from app.schemas.ai_decision_schema import AIDecisionSchema


class DecisionEngine:
    """
    Handles business decision logic.
    """

    def __init__(
        self,
        amount_threshold: float = 20.0,
        confidence_threshold: float = 90.0,
    ):

        self.amount_threshold = amount_threshold
        self.confidence_threshold = confidence_threshold

    def decide(
        self,
        difference: float,
        ai_decision: AIDecisionSchema,
    ) -> str:

        if difference <= self.amount_threshold:

            if ai_decision.confidence >= self.confidence_threshold:
                return "AUTO_CORRECT"

            return "HUMAN_REVIEW"

        return "RAISE_TICKET"