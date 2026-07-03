from pathlib import Path
from typing import Optional

from app.core.logger import logger
from app.tools.document.pdf_tool import PDFTool
from app.tools.document.ocr_tool import OCRTool


class DocumentProcessor:
    """
    Processes different document types and extracts text.
    """

    def __init__(self):
        self.pdf_tool = PDFTool()
        self.ocr_tool = OCRTool()

    def extract_text(self, file_path: str) -> Optional[str]:

        file_extension = Path(file_path).suffix.lower()

        if file_extension == ".pdf":
            logger.info("PDF detected.")
            return self.pdf_tool.extract_text(file_path)

        elif file_extension in [".png", ".jpg", ".jpeg"]:
            logger.info("Image detected.")
            return self.ocr_tool.extract_text(file_path)

        logger.error(f"Unsupported file type: {file_extension}")
        return None