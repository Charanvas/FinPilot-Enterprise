from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Float
from sqlalchemy import String

from app.core.database import Base


class PurchaseOrder(Base):

    __tablename__ = "purchase_orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )

    po_number = Column(
        String,
        unique=True,
    )

    vendor_name = Column(
        String,
        index=True,
    )

    expected_amount = Column(
        Float,
    )