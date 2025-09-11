from sqlalchemy import Column, Integer, String, Float, DECIMAL
from src.infrastructure.databases.base import Base

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    gold_weight = Column(Float, nullable=False)     # trọng lượng vàng (gram)
    gold_price = Column(DECIMAL(18, 2), nullable=False)  # giá vàng tại thời điểm (VNĐ/gram)
    labor_cost = Column(DECIMAL(18, 2), default=0)  # tiền công
    stone_cost = Column(DECIMAL(18, 2), default=0)  # tiền đá
    markup_ratio = Column(Float, default=1.2)       # tỉ lệ áp giá (ví dụ: 1.2 = 20%)
    final_price = Column(DECIMAL(18, 2), default=0) # giá bán cuối cùng

    def calculate_final_price(self):
        """Tính giá bán = (giá vàng * trọng lượng) + công + đá, sau đó nhân markup"""
        base_cost = (self.gold_price * self.gold_weight) + self.labor_cost + self.stone_cost
        self.final_price = base_cost * self.markup_ratio
        return self.final_price
