from ..databases.base import db
from datetime import datetime
from sqlalchemy import Numeric

class Promotion(db.Model):
    __tablename__ = "promotions"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    discount_percent = db.Column(Numeric(5, 2), default=0)  # ví dụ 10.00 = 10%
    start_date = db.Column(db.DateTime)
    end_date = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
