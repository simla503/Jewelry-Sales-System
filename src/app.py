from flask import Flask
from flasgger import Swagger
from src.infrastructure.databases import init_db
from src.config import SwaggerConfig

# import middleware nếu có
try:
    from src.api.middleware import middleware
except ImportError:
    middleware = None


def create_app():
    app = Flask(__name__)

    # init database
    init_db(app)

    # Swagger docs
    Swagger(app, template=SwaggerConfig.template, config=SwaggerConfig.swagger_config)

    # register middleware nếu có
    if middleware:
        middleware(app)

    # === Register blueprints ===
    from src.api.controllers.user_controller import bp as user_bp
    app.register_blueprint(user_bp, url_prefix="/users")

    from src.api.controllers.product_controller import bp as product_bp
    app.register_blueprint(product_bp, url_prefix="/products")

    return app


app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6868, debug=True)
