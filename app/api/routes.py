from fastapi import APIRouter, UploadFile, File, Form
import shutil
import os

from app.workflow.graph import graph

from app.tools.database.database_tool import DatabaseTool
from app.core.database import SessionLocal
from app.database.models import Ticket, AuditLog

router = APIRouter()

UPLOAD_FOLDER = "uploads"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

database = DatabaseTool()


# =====================================================
# Audit Invoice
# =====================================================
@router.post("/audit")
async def audit_invoice(
    file: UploadFile = File(...),
    expected_amount: float = Form(...),
):

    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename,
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    result = graph.invoke(
        {
            "file_path": file_path,
            "expected_amount": expected_amount,
            "invoice": None,
            "audit_result": None,
        }
    )

    return result["audit_result"].model_dump()


# =====================================================
# Invoice History
# =====================================================
@router.get("/invoices")
def get_invoices():

    invoices = database.get_all_invoices()

    return [
        {
            "invoice_number": invoice.invoice_number,
            "vendor_name": invoice.vendor_name,
            "invoice_date": str(invoice.invoice_date),
            "expected_amount": invoice.expected_amount,
            "invoice_total": invoice.actual_amount,
            "status": invoice.status,
            "created_at": str(invoice.created_at),
        }
        for invoice in invoices
    ]


# =====================================================
# Tickets
# =====================================================
@router.get("/tickets")
def get_tickets():

    db = SessionLocal()

    try:

        tickets = db.query(Ticket).all()

        return [
            {
                "ticket_id": ticket.id,
                "invoice_id": ticket.invoice_id,
                "priority": ticket.priority,
                "status": ticket.status,
                "description": ticket.description,
                "created_at": str(ticket.created_at),
            }
            for ticket in tickets
        ]

    finally:

        db.close()


# =====================================================
# Audit Logs
# =====================================================
@router.get("/audit-logs")
def get_audit_logs():

    db = SessionLocal()

    try:

        logs = db.query(AuditLog).all()

        return [
            {
                "id": log.id,
                "invoice_id": log.invoice_id,
                "action": log.action,
                "performed_by": log.performed_by,
                "timestamp": str(log.timestamp),
            }
            for log in logs
        ]

    finally:

        db.close()


# =====================================================
# Health Check
# =====================================================
@router.get("/")
def home():

    return {
        "message": "Welcome to FinPilot API 🚀"
    }
# =====================================================
# Dashboard Analytics
# =====================================================
@router.get("/analytics")
def get_analytics():

    from app.tools.database.database_tool import DatabaseTool

    database = DatabaseTool()

    invoices = database.get_all_invoices()

    total_invoices = len(invoices)

    auto_corrected = 0
    tickets_raised = 0

    money_audited = 0
    vendors = set()

    highest_invoice = 0

    for invoice in invoices:

        # Your database model stores actual invoice amount here
        amount = invoice.actual_amount

        money_audited += amount

        vendors.add(invoice.vendor_name)

        if amount > highest_invoice:
            highest_invoice = amount

        if invoice.status == "AUTO_CORRECT":
            auto_corrected += 1

        elif invoice.status == "RAISE_TICKET":
            tickets_raised += 1

    average_invoice = 0

    if total_invoices > 0:

        average_invoice = (
            money_audited / total_invoices
        )

    success_rate = 0

    if total_invoices > 0:

        success_rate = round(

            auto_corrected
            /
            total_invoices
            * 100,

            2,

        )

    return {

        "total_invoices": total_invoices,

        "money_audited": round(
            money_audited,
            2,
        ),

        "auto_corrected": auto_corrected,

        "tickets_raised": tickets_raised,

        "vendors": len(vendors),

        "average_invoice": round(
            average_invoice,
            2,
        ),

        "highest_invoice": round(
            highest_invoice,
            2,
        ),

        "success_rate": success_rate,

    }