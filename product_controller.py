from flask import Blueprint, request, jsonify
from api.schemas.product_schema import ProductSchema

bp = Blueprint('product', __name__, url_prefix='/products')

PRODUCTS = []
product_schema = ProductSchema()
product_list_schema = ProductSchema(many=True)

def is_admin():
    # Giả lập kiểm tra quyền admin, thực tế nên kiểm tra JWT/token/session
    return request.headers.get('X-Role') == 'admin'

@bp.route('/', methods=['GET'])
def get_products():
    return jsonify(product_list_schema.dump(PRODUCTS)), 200

@bp.route('/', methods=['POST'])
def add_product():
    if not is_admin():
        return jsonify({'message': 'Chỉ Admin được phép thêm sản phẩm'}), 403
    data = request.get_json()
    errors = product_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    data['id'] = len(PRODUCTS) + 1
    PRODUCTS.append(data)
    return jsonify(product_schema.dump(data)), 201

@bp.route('/<int:id>', methods=['GET'])
def get_product(id):
    for product in PRODUCTS:
        if product['id'] == id:
            return jsonify(product_schema.dump(product)), 200
    return jsonify({'message': 'Không tìm thấy sản phẩm'}), 404

@bp.route('/<int:id>', methods=['PUT'])
def update_product(id):
    if not is_admin():
        return jsonify({'message': 'Chỉ Admin được phép cập nhật sản phẩm'}), 403
    for product in PRODUCTS:
        if product['id'] == id:
            data = request.get_json()
            errors = product_schema.validate(data)
            if errors:
                return jsonify(errors), 400
            product.update(data)
            product['id'] = id
            return jsonify(product_schema.dump(product)), 200
    return jsonify({'message': 'Không tìm thấy sản phẩm'}), 404

@bp.route('/<int:id>', methods=['DELETE'])
def delete_product(id):
    if not is_admin():
        return jsonify({'message': 'Chỉ Admin được phép xóa sản phẩm'}), 403
    for i, product in enumerate(PRODUCTS):
        if product['id'] == id:
            del PRODUCTS[i]
            return jsonify({'message': 'Đã xóa sản phẩm'}), 200
    return jsonify({'message': 'Không tìm thấy sản phẩm'}), 404