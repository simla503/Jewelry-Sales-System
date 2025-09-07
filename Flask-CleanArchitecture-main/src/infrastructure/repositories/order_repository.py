from ..databases.base import db
from ..models.order_model import Order
from ..models.order_detail_model import OrderDetail

class OrderRepository:
    def create(self, **data) -> Order:
        try:
            obj = Order(**data)
            db.session.add(obj)
            db.session.commit()
            return obj
        except Exception as e:
            db.session.rollback()
            raise e

    def get_all(self):
        return Order.query.order_by(Order.id.desc()).all()

    def get_by_id(self, oid: int):
        return Order.query.get(oid)

    def update(self, oid: int, **data):
        try:
            obj = Order.query.get(oid)
            if not obj:
                return None
            for k, v in data.items():
                setattr(obj, k, v)
            db.session.commit()
            return obj
        except Exception as e:
            db.session.rollback()
            raise e

    def delete(self, oid: int) -> bool:
        try:
            obj = Order.query.get(oid)
            if not obj:
                return False
            db.session.delete(obj)  # nhờ cascade -> OrderDetail sẽ tự xóa
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise e

    def add_detail(self, order_id: int, **data) -> OrderDetail:
        try:
            d = OrderDetail(order_id=order_id, **data)
            db.session.add(d)
            db.session.commit()
            return d
        except Exception as e:
            db.session.rollback()
            raise e
