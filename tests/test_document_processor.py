from app.tools.document.document_processor import DocumentProcessor

processor = DocumentProcessor()

text = processor.extract_text("uploads/invoice.pdf")

print(text[:500])