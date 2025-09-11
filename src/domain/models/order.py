from sqlalchemy import Column, Integer, ForeignKey, DateTime, DECIMAL
from datetime import datetime
from src.infrastructure.databases.base import Base

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    total_price = Column(DECIMAL(18, 2), nullable=False, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
