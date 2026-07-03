from app.tools.ticket.ticket_tool import TicketTool

tool = TicketTool()

ticket = tool.create_ticket(
    invoice_id=1,
    description="Difference exceeds threshold.",
)

print(ticket.id)
print(ticket.status)
print(ticket.priority)

tool.close()