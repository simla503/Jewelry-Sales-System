from src.models.product_model import Product
from src.models.order_model import Order, OrderDetail
from src.database import db

def create_order(user_id, items):
    total_price = 0
    order = Order(user_id=user_id, total_price=0)
    db.session.add(order)
    db.session.commit()

    for item in items:
        product = Product.query.get(item["product_id"])
        if not product:
            raise Exception("Product not found")
        if product.stock < item["quantity"]:
            raise Exception("Not enough stock")

        price = product.price * item["quantity"]
        total_price += price

        detail = OrderDetail(
            order_id=order.id,
            product_id=product.id,
            quantity=item["quantity"],
            price=price
        )
        db.session.add(detail)

        # giảm tồn kho
        product.stock -= item["quantity"]

    order.total_price = total_price
    db.session.commit()
    return order.to_dict()

def get_orders(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()
    return [o.to_dict() for o in orders]

def get_order_detail(order_id):
    order = Order.query.get(order_id)
    return order.to_dict() if order else None
