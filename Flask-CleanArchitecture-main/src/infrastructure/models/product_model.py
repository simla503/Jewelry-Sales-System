from ..databases.base import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = "products"
    id = db.Column(db.Integer, primary_key=True)
    sku = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    karat = db.Column(db.String(10))
    weight_gram = db.Column(db.Float, default=0)
    labor_cost = db.Column(db.Integer, default=0)
    stone_cost = db.Column(db.Integer, default=0)
    price_ratio = db.Column(db.Float, default=1.10)
    counter_code = db.Column(db.String(20))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
