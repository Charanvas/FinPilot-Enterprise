from app.tools.document.pdf_tool import PDFTool


pdf_tool = PDFTool()

text = pdf_tool.extract_text("uploads/invoice.pdf")

print(text)