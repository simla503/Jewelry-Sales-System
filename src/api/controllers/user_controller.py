from flask import Blueprint, request, jsonify
from src.services.user_service import UserService
from src.api.middleware import token_required

bp = Blueprint("users", __name__)
user_service = UserService()


@bp.route("/users/register", methods=["POST"])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    role = data.get("role", "Staff")

    user, error = user_service.register_user(name, email, password, role)
    if error:
        return jsonify({"message": error}), 400

    return jsonify({"id": user.id, "name": user.name, "email": user.email, "role": user.role}), 201


@bp.route("/users/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    token, error = user_service.login_user(email, password)
    if error:
        return jsonify({"message": error}), 401

    return jsonify({"token": token}), 200


@bp.route("/users/me", methods=["GET"])
@token_required
def me(current_user_id):
    user = user_service.get_user_by_id(current_user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify({"id": user.id, "name": user.name, "email": user.email, "role": user.role}), 200
