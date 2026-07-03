from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    DateTime,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from datetime import datetime

from app.core.database import Base


# =====================================================
# Invoice Table
# =====================================================
class Invoice(Base):
    __tablename__ = "invoices"

    id = Column(Integer, primary_key=True, index=True)

    invoice_number = Column(String, unique=True, nullable=False)
    vendor_name = Column(String, nullable=False)

    invoice_date = Column(DateTime)
    expected_amount = Column(Float, nullable=False)
    actual_amount = Column(Float, nullable=False)

    status = Column(String, default="Pending")
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    corrections = relationship("Correction", back_populates="invoice")
    tickets = relationship("Ticket", back_populates="invoice")
    audit_logs = relationship("AuditLog", back_populates="invoice")


# =====================================================
# Correction Table
# =====================================================
class Correction(Base):
    __tablename__ = "corrections"

    id = Column(Integer, primary_key=True, index=True)

    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    old_amount = Column(Float)
    new_amount = Column(Float)

    reason = Column(String)
    confidence = Column(Float)

    corrected_at = Column(DateTime, default=datetime.utcnow)

    invoice = relationship("Invoice", back_populates="corrections")


# =====================================================
# Ticket Table
# =====================================================
class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, primary_key=True, index=True)

    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    priority = Column(String)
    status = Column(String, default="Open")
    description = Column(String)

    created_at = Column(DateTime, default=datetime.utcnow)

    invoice = relationship("Invoice", back_populates="tickets")


# =====================================================
# Audit Log Table
# =====================================================
class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)

    invoice_id = Column(Integer, ForeignKey("invoices.id"))

    action = Column(String)
    performed_by = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    invoice = relationship("Invoice", back_populates="audit_logs")