from pathlib import Path
from typing import Optional

import pytesseract
from PIL import Image

from app.core.logger import logger


class OCRTool:
    """
    Tool for extracting text from image-based invoices.
    """

    def __init__(self):
        pass

    def extract_text(self, image_path: str) -> Optional[str]:
        """
        Extract text from an image.

        Args:
            image_path (str): Path to image.

        Returns:
            Optional[str]: Extracted text or None.
        """

        try:

            image_file = Path(image_path)

            if not image_file.exists():
                logger.error(f"Image not found: {image_path}")
                return None

            image = Image.open(image_file)

            text = pytesseract.image_to_string(image)

            logger.info("OCR extraction completed successfully.")

            return text.strip()

        except Exception as e:
            logger.error(f"OCR extraction failed: {e}")
            return None