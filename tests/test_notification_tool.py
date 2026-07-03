from app.tools.notification.notification_tool import NotificationTool

tool = NotificationTool()

tool.send_notification(
    title="Invoice Processed",
    message="Invoice INV001 was auto-corrected successfully.",
)