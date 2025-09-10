from ..databases.base import db
from datetime import datetime
from sqlalchemy import Numeric

class LoyaltyTransaction(db.Model):
    __tablename__ = "loyalty_transactions"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    points = db.Column(Numeric(18, 2), default=0)
    description = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
