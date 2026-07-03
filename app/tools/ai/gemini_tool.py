import json
from pathlib import Path

from langchain_google_genai import ChatGoogleGenerativeAI

from app.core.config import settings
from app.core.logger import logger
from app.schemas.ai_decision_schema import AIDecisionSchema


class GeminiTool:
    """
    Enterprise wrapper for Gemini AI.
    """

    def __init__(self):

        self.model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            google_api_key=settings.GEMINI_API_KEY,
            temperature=0,
        )

    def _load_prompt(self):

        return Path(
            "app/prompts/finance_prompt.txt"
        ).read_text(
            encoding="utf-8"
        )

    def analyze(self, invoice_data: str):

        try:

            prompt = self._load_prompt()

            final_prompt = f"""

{prompt}

Invoice Data:

{invoice_data}

"""

            response = self.model.invoke(final_prompt)

            logger.info("Gemini analysis completed.")

            data = json.loads(response.content)

            return AIDecisionSchema(**data)

        except Exception as e:

            logger.error(e)

            return None