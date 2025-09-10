from ..databases.base import db
from datetime import datetime
from sqlalchemy import Numeric

class Order(db.Model):
    __tablename__ = "orders"

    id = db.Column(db.Integer, primary_key=True)
    invoice_no = db.Column(db.String(30), unique=True, nullable=False)
    customer_id = db.Column(db.Integer)

    # Dùng Numeric để lưu số tiền chính xác
    subtotal = db.Column(Numeric(18, 2), default=0)
    discount = db.Column(Numeric(18, 2), default=0)
    total = db.Column(Numeric(18, 2), default=0)

    created_by = db.Column(db.Integer)   # staff_id
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Quan hệ 1-nhiều với OrderDetail
    order_details = db.relationship(
        "OrderDetail",
        back_populates="order",
        cascade="all, delete-orphan"
    )
