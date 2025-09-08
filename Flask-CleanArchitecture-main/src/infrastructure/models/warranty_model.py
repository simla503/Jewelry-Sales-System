from ..databases.base import db
from datetime import datetime

class Warranty(db.Model):
    __tablename__ = "warranties"

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    duration_months = db.Column(db.Integer, default=12)  # mặc định 12 tháng
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
