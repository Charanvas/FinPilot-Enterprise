from sqlalchemy.orm import Session

from app.core.database import SessionLocal

from app.database.models.purchase_order import PurchaseOrder


class PurchaseOrderTool:

    def __init__(self):

        self.db: Session = SessionLocal()

    def get_expected_amount(
        self,
        vendor_name,
    ):

        po = (

            self.db.query(
                PurchaseOrder
            )

            .filter(
                PurchaseOrder.vendor_name == vendor_name
            )

            .first()

        )

        if po:

            return po.expected_amount

        return None