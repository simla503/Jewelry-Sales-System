from src.domain.models.product import Product
from src.infrastructure.repositories.product_repository import ProductRepository

class ProductService:
    def __init__(self):
        self.repo = ProductRepository()

    def create_product(self, data):
        product = Product(
            name=data["name"],
            gold_weight=data["gold_weight"],
            gold_price=data["gold_price"],
            labor_cost=data.get("labor_cost", 0),
            stone_cost=data.get("stone_cost", 0),
            markup_ratio=data.get("markup_ratio", 1.2),
        )
        product.calculate_final_price()
        return self.repo.add(product)

    def list_products(self):
        return self.repo.get_all()

    def get_product(self, product_id: int):
        return self.repo.get_by_id(product_id)

    def update_product(self, product_id: int, data):
        product = self.repo.get_by_id(product_id)
        if not product:
            return None
        product.name = data.get("name", product.name)
        product.gold_weight = data.get("gold_weight", product.gold_weight)
        product.gold_price = data.get("gold_price", product.gold_price)
        product.labor_cost = data.get("labor_cost", product.labor_cost)
        product.stone_cost = data.get("stone_cost", product.stone_cost)
        product.markup_ratio = data.get("markup_ratio", product.markup_ratio)

        product.calculate_final_price()
        return self.repo.update(product)

    def delete_product(self, product_id: int):
        product = self.repo.get_by_id(product_id)
        if not product:
            return None
        self.repo.delete(product)
        return product
