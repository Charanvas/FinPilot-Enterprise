from app.tools.ai.gemini_tool import GeminiTool

tool = GeminiTool()

invoice = """
Vendor: McDonald's

Invoice Total: 395.99

Expected Amount: 400
"""

result = tool.analyze(invoice)

print(result)

print(result.model_dump())