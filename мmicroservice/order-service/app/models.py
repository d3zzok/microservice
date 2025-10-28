from sqlalchemy import Column, Integer, String, DateTime, JSON, Float
from .database import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    phone = Column(String)
    created_at = Column(DateTime)
    address = Column(JSON)

class Cart(Base):
    __tablename__ = "carts"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    items = Column(JSON)
    updated_at = Column(DateTime)

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    status = Column(String)
    total_amount = Column(Float)
    created_at = Column(DateTime)
    items = Column(JSON)
    shipping_address = Column(JSON)