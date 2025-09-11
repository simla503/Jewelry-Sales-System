import jwt
import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from src.config import Config
from src.infrastructure.repositories.user_repository import UserRepository
from src.domain.models.user import User
from src.infrastructure.databases.mssql import SessionLocal


class UserService:
    def __init__(self):
        self.db = SessionLocal()
        self.repo = UserRepository(self.db)

    def register_user(self, name, email, password, role="Staff"):
        # Kiểm tra email đã tồn tại chưa
        if self.repo.get_by_email(email):
            return None, "Email already registered"

        hashed_password = generate_password_hash(password)
        user = User(name=name, email=email, password=hashed_password, role=role)
        self.repo.create(user)
        return user, None

    def login_user(self, email, password):
        user = self.repo.get_by_email(email)
        if not user:
            return None, "User not found"

        if not check_password_hash(user.password, password):
            return None, "Invalid password"

        token = jwt.encode(
            {
                "user_id": user.id,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2),
            },
            Config.JWT_SECRET_KEY,
            algorithm="HS256",
        )
        return token, None

    def get_user_by_id(self, user_id):
        return self.repo.get_by_id(user_id)
