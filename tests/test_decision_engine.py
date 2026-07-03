from app.schemas.ai_decision_schema import AIDecisionSchema
from app.services.decision_engine import DecisionEngine

engine = DecisionEngine()

decision = AIDecisionSchema(
    status="AUTO_CORRECT",
    confidence=95,
    reason="Difference below threshold.",
    correct_amount=400,
)

result = engine.decide(
    difference=4,
    ai_decision=decision,
)

print(result)