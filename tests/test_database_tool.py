from datetime import datetime

from app.schemas.invoice_schema import InvoiceSchema
from app.tools.database.database_tool import DatabaseTool

db = DatabaseTool()

invoice = InvoiceSchema(
    invoice_number="INV001",
    vendor_name="Amazon",
    invoice_date=datetime(2026, 7, 2),   # ✅ Correct
    invoice_total=399.99,
)

saved = db.save_invoice(
    invoice=invoice,
    expected_amount=400,
    status="AUTO_CORRECT",
)

print(saved.invoice_number)

db.close()