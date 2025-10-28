import os
import time
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

def wait_for_db():
    database_url = os.getenv("DATABASE_URL", "postgresql://user:password@payment-db:5432/paymentdb")
    engine = create_engine(database_url)
    
    for i in range(30):
        try:
            with engine.connect() as conn:
                print("✅ Database is ready!")
                return True
        except OperationalError:
            print(f"⏳ Waiting for database... Attempt {i+1}/30")
            time.sleep(2)
    
    print("❌ Database connection failed after 30 attempts")
    return False

if not wait_for_db():
    exit(1)

from .database import engine
from . import models

try:
    models.Base.metadata.create_all(bind=engine)
    print("✅ Database tables created successfully")
except Exception as e:
    print(f"❌ Error creating database tables: {e}")
    exit(1)

app = FastAPI(title="Payment Service", version="1.0.0")

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "payment-service"}

print("🚀 Payment Service started successfully!")