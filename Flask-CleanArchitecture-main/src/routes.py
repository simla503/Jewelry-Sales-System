from src.api.controllers.order_controller import order_bp

def register_routes(app):
    app.register_blueprint(order_bp)
    # các blueprint khác
