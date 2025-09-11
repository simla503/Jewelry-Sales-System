from src.infrastructure.databases.mssql import engine, SessionLocal, init_mssql

# Alias tiện dụng cho code cũ dùng init_db
def init_db(app=None):
    return init_mssql(app)
