from app.tools.document.pdf_tool import PDFTool
from app.tools.document.invoice_parser_tool import InvoiceParserTool

pdf_tool = PDFTool()
parser = InvoiceParserTool()

text = pdf_tool.extract_text("uploads/invoice.pdf")

result = parser.extract(text)

print(result.invoice_number)
print(result.vendor_name)
print(result.invoice_date)
print(result.invoice_total)