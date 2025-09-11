from sqlalchemy import Column, Integer, ForeignKey, DECIMAL
from src.infrastructure.databases.base import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("orders.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(DECIMAL(18, 2), nullable=False, default=0)
