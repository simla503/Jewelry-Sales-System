from ..databases.base import db
from sqlalchemy import Numeric

class OrderDetail(db.Model):
    __tablename__ = "order_details"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("orders.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    qty = db.Column(db.Integer, default=1)

    # Giá và thành tiền -> dùng Numeric để chính xác
    unit_price = db.Column(Numeric(18, 2), default=0)
    line_total = db.Column(Numeric(18, 2), default=0)

    # Quan hệ với Order và Product
    order = db.relationship("Order", back_populates="order_details")
    product = db.relationship("Product", back_populates="order_details")
