from app.core.logger import logger


class NotificationTool:
    """
    Handles notifications after invoice processing.
    """

    def send_notification(
        self,
        title: str,
        message: str,
    ) -> None:

        logger.info("=" * 50)
        logger.info(f"NOTIFICATION: {title}")
        logger.info(message)
        logger.info("=" * 50)