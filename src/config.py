# Configuration settings for the Flask application

import os
import urllib.parse

class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecret'
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwtsecret")
    DEBUG = os.environ.get('DEBUG', 'False').lower() in ['true', '1']
    TESTING = os.environ.get('TESTING', 'False').lower() in ['true', '1']
    CORS_HEADERS = 'Content-Type'

    # ======================
    # DATABASE CONFIG
    # ======================

    # --- SQLite fallback ---
    SQLITE_URI = os.getenv("SQLITE_URI") or "sqlite:///dev.db"

    # --- SQL Server (Docker) ---
    DB_USER = os.getenv("DB_USER", "sa")
    DB_PASSWORD_RAW = os.getenv("DB_PASSWORD", "Aa@123456")
    DB_PASSWORD = urllib.parse.quote_plus(DB_PASSWORD_RAW)  # encode mật khẩu có ký tự đặc biệt
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "1433")
    DB_NAME = os.getenv("DB_NAME", "JewelryDB")

    # Connection string MSSQL
    MSSQL_URI = (
    f"mssql+pyodbc://{DB_USER}:{DB_PASSWORD}@127.0.0.1,1433/{DB_NAME}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
)





    # Chọn DB engine: nếu có USE_MSSQL=true thì dùng SQL Server, ngược lại dùng SQLite
    if os.getenv("USE_MSSQL", "false").lower() in ["true", "1", "yes"]:
        DB_URI = MSSQL_URI
    else:
        DB_URI = SQLITE_URI

    # Giữ tương thích với code cũ (DATABASE_URI)
    DATABASE_URI = DB_URI


class DevelopmentConfig(Config):
    """Development configuration."""
    DEBUG = True


class TestingConfig(Config):
    """Testing configuration."""
    TESTING = True
    DATABASE_URI = "sqlite:///test.db"  # luôn dùng SQLite cho test


class ProductionConfig(Config):
    """Production configuration."""
    DEBUG = False


# ======================
# SWAGGER CONFIG
# ======================

template = {
    "swagger": "2.0",
    "info": {
        "title": "Jewelry Sales System API",
        "description": "API for managing users, products, and orders at a jewelry store",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": ["http", "https"],
    "consumes": ["application/json"],
    "produces": ["application/json"]
}

class SwaggerConfig:
    """Swagger configuration."""
    template = template
    swagger_config = {
        "headers": [],
        "specs": [
            {
                "endpoint": 'apispec',
                "route": '/apispec.json',
                "rule_filter": lambda rule: True,
                "model_filter": lambda tag: True,
            }
        ],
        "static_url_path": "/flasgger_static",
        "swagger_ui": True,
        "specs_route": "/docs"
    }
