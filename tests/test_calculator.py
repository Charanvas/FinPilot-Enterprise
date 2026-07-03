from app.tools.finance.calculator_tool import CalculatorTool

calculator = CalculatorTool()

result = calculator.compare_amounts(
    expected_amount=400,
    actual_amount=395.99
)

print(result)