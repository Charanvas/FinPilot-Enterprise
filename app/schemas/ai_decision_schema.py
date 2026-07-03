from typing import Optional

from pydantic import BaseModel, Field


class AIDecisionSchema(BaseModel):
    """
    Standard AI decision returned by Gemini.
    """

    status: str = Field(
        description="AUTO_CORRECT, HUMAN_REVIEW or APPROVED"
    )

    confidence: float = Field(
        ge=0,
        le=100,
        description="Confidence score"
    )

    reason: str = Field(
        description="Reason for the decision"
    )

    correct_amount: Optional[float] = Field(
        default=None,
        description="Suggested corrected amount"
    )