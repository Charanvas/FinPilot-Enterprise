from app.tools.document.ocr_tool import OCRTool

ocr = OCRTool()

text = ocr.extract_text("uploads/invoice_image.jpg")

print(text)