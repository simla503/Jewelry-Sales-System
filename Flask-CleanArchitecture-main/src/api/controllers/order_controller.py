from flask import Blueprint, request, jsonify
from src.services import order_service

order_bp = Blueprint("orders", __name__)

# POST /orders
@order_bp.route("/orders", methods=["POST"])
def create_order():
    data = request.json
    user_id = data.get("user_id")
    items = data.get("items", [])
    order = order_service.create_order(user_id, items)
    return jsonify(order), 201

# GET /orders
@order_bp.route("/orders", methods=["GET"])
def list_orders():
    user_id = request.args.get("user_id")
    orders = order_service.get_orders(user_id)
    return jsonify(orders), 200

# GET /orders/{id}
@order_bp.route("/orders/<int:order_id>", methods=["GET"])
def order_detail(order_id):
    order = order_service.get_order_detail(order_id)
    if not order:
        return jsonify({"error": "Order not found"}), 404
    return jsonify(order), 200
