import jwt
from functools import wraps
from flask import request, jsonify
from src.config import Config


def token_required(f):
    """Middleware kiểm tra JWT token."""
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # Lấy token từ header Authorization: Bearer <token>
        if "Authorization" in request.headers:
            auth_header = request.headers["Authorization"]
            if auth_header.startswith("Bearer "):
                token = auth_header.split(" ")[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, Config.JWT_SECRET_KEY, algorithms=["HS256"])
            current_user_id = data["user_id"]
        except Exception as e:
            return jsonify({"message": "Token is invalid!", "error": str(e)}), 401

        # Truyền current_user_id xuống cho route
        return f(current_user_id, *args, **kwargs)

    return decorated
