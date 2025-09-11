import pyodbc

server = '127.0.0.1,1433'
database = 'master'  # connect vào master để tạo DB mới
username = 'sa'
password = 'Aa@123456'
driver = 'ODBC Driver 17 for SQL Server'

conn = pyodbc.connect(
    f"DRIVER={{{driver}}};SERVER={server};UID={username};PWD={password};DATABASE={database}"
)
cursor = conn.cursor()

cursor.execute("IF NOT EXISTS(SELECT name FROM sys.databases WHERE name = 'JewelryDB') CREATE DATABASE JewelryDB;")
conn.commit()

print("✅ Database JewelryDB created or already exists.")
conn.close()
