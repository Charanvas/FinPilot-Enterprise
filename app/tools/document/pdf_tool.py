import fitz
from pathlib import Path
from typing import Optional

from app.core.logger import logger


class PDFTool:
    """
    Tool for extracting text from PDF invoices.
    """

    def __init__(self):
        pass

    def extract_text(self, pdf_path: str) -> Optional[str]:
        """
        Extract text from a PDF file.

        Args:
            pdf_path (str): Path to the PDF.

        Returns:
            str | None: Extracted text or None if extraction fails.
        """

        try:
            pdf_file = Path(pdf_path)

            if not pdf_file.exists():
                logger.error(f"PDF not found: {pdf_path}")
                return None

            document = fitz.open(pdf_file)

            text = ""

            for page in document:
                text += page.get_text()

            document.close()

            logger.info("PDF text extracted successfully.")

            return text.strip()

        except Exception as e:
            logger.error(f"PDF extraction failed: {e}")
            return None