from ..databases.base import db
from ..models.product_model import Product

class ProductRepository:
    def create(self, **data) -> Product:
        try:
            obj = Product(**data)
            db.session.add(obj)
            db.session.commit()
            return obj
        except Exception as e:
            db.session.rollback()
            raise e

    def get_all(self):
        return Product.query.order_by(Product.id.desc()).all()

    def get_by_id(self, pid: int):
        return Product.query.get(pid)

    def update(self, pid: int, **data):
        try:
            obj = Product.query.get(pid)
            if not obj:
                return None
            for k, v in data.items():
                setattr(obj, k, v)
            db.session.commit()
            return obj
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self, pid: int) -> bool:
        try:
            obj = Product.query.get(pid)
            if not obj:
                return False
            db.session.delete(obj)
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e
