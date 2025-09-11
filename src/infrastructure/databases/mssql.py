from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.config import Config
from src.infrastructure.databases.base import Base
import importlib

# Lấy URL kết nối (ưu tiên DB_URI, tương thích với DATABASE_URI cũ)
DATABASE_URL = getattr(Config, "DB_URI", None) or getattr(Config, "DATABASE_URI", None)
print(f"[DB] Connecting to: {DATABASE_URL}")

# Tạo engine
engine = create_engine(
    DATABASE_URL,
    echo=True,    # In câu SQL để debug
    future=True   # Dùng SQLAlchemy 2.x style
)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def _safe_import(module_path: str):
    """
    Import module một cách an toàn (không làm app crash nếu module chưa tồn tại).
    Dùng cho các model tuỳ bạn đã tạo xong hay chưa.
    """
    try:
        importlib.import_module(module_path)
        print(f"[DB] Loaded model module: {module_path}")
    except ModuleNotFoundError as e:
        print(f"[DB] (Optional) Model module not found: {module_path} ({e})")
    except Exception as e:
        print(f"[DB] Error importing {module_path}: {e}")

def init_mssql(app=None):
    """
    Khởi tạo database:
    - Import các model để SQLAlchemy đăng ký metadata
    - Tạo bảng nếu chưa có
    """
    # Import các model cốt lõi (bạn thêm/bớt tuỳ theo file bạn đã có)
    for module in [
        "src.domain.models.user",
        "src.domain.models.product",
        "src.domain.models.order",
        "src.domain.models.order_detail",
        # Có thể bổ sung dần:
        # "src.domain.models.customer_model",
        # "src.domain.models.promotion_model",
        # "src.domain.models.warranty_model",
        # "src.domain.models.buyback_model",
        # "src.domain.models.loyalty_transaction_model",
    ]:
        _safe_import(module)

    # Tạo bảng
    Base.metadata.create_all(bind=engine)
