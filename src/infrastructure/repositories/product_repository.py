from src.domain.models.product import Product
from src.infrastructure.databases.mssql import SessionLocal

class ProductRepository:
    def __init__(self):
        self.db = SessionLocal()

    def add(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)
        return product

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int):
        return self.db.query(Product).filter(Product.id == product_id).first()

    def update(self, product: Product):
        self.db.commit()
        self.db.refresh(product)
        return product

    def delete(self, product: Product):
        self.db.delete(product)
        self.db.commit()
