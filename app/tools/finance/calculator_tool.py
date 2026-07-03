from typing import Dict


class CalculatorTool:
    """
    Financial calculation tool.
    """

    def __init__(self, threshold: float = 20.0):
        self.threshold = threshold

    def compare_amounts(
        self,
        expected_amount: float,
        actual_amount: float
    ) -> Dict:

        difference = abs(expected_amount - actual_amount)

        return {
            "expected_amount": expected_amount,
            "actual_amount": actual_amount,
            "difference": round(difference, 2),
            "within_threshold": difference <= self.threshold
        }