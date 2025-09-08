from ..databases.base import db
from datetime import datetime
from sqlalchemy import Numeric

class BuyBack(db.Model):
    __tablename__ = "buybacks"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    price = db.Column(Numeric(18, 2), default=0)  # giá mua lại
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
