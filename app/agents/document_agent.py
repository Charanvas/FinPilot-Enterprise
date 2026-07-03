from app.tools.document.document_processor import DocumentProcessor
from app.tools.document.invoice_parser_tool import InvoiceParserTool

from app.schemas.invoice_schema import InvoiceSchema

from app.core.logger import logger


class DocumentAgent:
    """
    Responsible for extracting structured invoice data.
    """

    def __init__(self):

        self.processor = DocumentProcessor()

        self.parser = InvoiceParserTool()

    def process(
        self,
        file_path: str,
    ) -> InvoiceSchema:

        logger.info("Document Agent started.")

        raw_text = self.processor.extract_text(file_path)

        invoice = self.parser.extract(raw_text)

        logger.info("Document Agent completed.")

        return invoice