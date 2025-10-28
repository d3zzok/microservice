import os
import time
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

# Функция для ожидания готовности базы данных
def wait_for_db():
    database_url = os.getenv("DATABASE_URL", "postgresql://user:password@order-db:5432/orderdb")
    engine = create_engine(database_url)
    
    for i in range(30):  # Пытаемся подключиться 30 раз с интервалом 2 секунды
        try:
            with engine.connect() as conn:
                print("✅ Database is ready!")
                return True
        except OperationalError:
            print(f"⏳ Waiting for database... Attempt {i+1}/30")
            time.sleep(2)
    
    print("❌ Database connection failed after 30 attempts")
    return False

# Ждем готовность базы данных перед запуском приложения
if not wait_for_db():
    exit(1)

from .database import engine
from . import models

# Создание таблиц
try:
    models.Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")
except Exception as e:
    print(f"❌ Error creating database tables: {e}")
    exit(1)

app = FastAPI(title="Order Service", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "order-service"}
from .routers import users, orders

app.include_router(users.router, prefix="/api/v1/users", tags=["users"])
app.include_router(orders.router, prefix="/api/v1/orders", tags=["orders"])
print("🚀 Order Service started successfully!")