from flask import Blueprint, request, jsonify
from src.services.product_service import ProductService

bp = Blueprint("products", __name__)
service = ProductService()


@bp.route("/", methods=["POST"])
def create_product():
    """
    Tạo sản phẩm mới
    ---
    tags:
      - Products
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            gold_weight:
              type: number
            gold_price:
              type: number
            labor_cost:
              type: number
            stone_cost:
              type: number
            markup_ratio:
              type: number
    responses:
      201:
        description: Sản phẩm được tạo thành công
    """
    data = request.get_json()
    product = service.create_product(data)
    return jsonify({
        "id": product.id,
        "name": product.name,
        "final_price": float(product.final_price)
    }), 201


@bp.route("/", methods=["GET"])
def list_products():
    """
    Lấy danh sách tất cả sản phẩm
    ---
    tags:
      - Products
    responses:
      200:
        description: Danh sách sản phẩm
    """
    products = service.list_products()
    return jsonify([
        {
            "id": p.id,
            "name": p.name,
            "final_price": float(p.final_price)
        }
        for p in products
    ])


@bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    """
    Lấy thông tin chi tiết sản phẩm theo ID
    ---
    tags:
      - Products
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Thông tin sản phẩm
      404:
        description: Không tìm thấy sản phẩm
    """
    product = service.get_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({
        "id": product.id,
        "name": product.name,
        "final_price": float(product.final_price)
    })


@bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    """
    Cập nhật thông tin sản phẩm
    ---
    tags:
      - Products
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            gold_weight:
              type: number
            gold_price:
              type: number
            labor_cost:
              type: number
            stone_cost:
              type: number
            markup_ratio:
              type: number
    responses:
      200:
        description: Sản phẩm đã được cập nhật
      404:
        description: Không tìm thấy sản phẩm
    """
    data = request.get_json()
    product = service.update_product(product_id, data)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({
        "id": product.id,
        "name": product.name,
        "final_price": float(product.final_price)
    })


@bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    """
    Xóa sản phẩm
    ---
    tags:
      - Products
    parameters:
      - name: product_id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Sản phẩm đã bị xóa
      404:
        description: Không tìm thấy sản phẩm
    """
    product = service.delete_product(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"message": "Product deleted successfully"})
