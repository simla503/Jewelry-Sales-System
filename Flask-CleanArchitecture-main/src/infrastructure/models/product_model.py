from ..databases.base import db
from datetime import datetime
from sqlalchemy import Numeric

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    karat = db.Column(db.String(10))

    weight_gram = db.Column(db.Float, default=0)

    # Chi phí -> dùng Numeric(18,2) thay cho Integer
    labor_cost = db.Column(Numeric(18, 2), default=0)
    stone_cost = db.Column(Numeric(18, 2), default=0)

    # Hệ số nhân giá (markup factor) -> default = 1.00
    price_ratio = db.Column(Numeric(5, 2), default=1.00)

    # Giá vàng tại thời điểm bán (theo ERD gốc)
    gold_price_at_sale = db.Column(Numeric(18, 2))

    # Giá cuối cùng (gold_price_at_sale + labor_cost + stone_cost)
    final_price = db.Column(Numeric(18, 2))

    counter_code = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Nếu muốn tham chiếu sang OrderDetail
    order_details = db.relationship("OrderDetail", back_populates="product")
