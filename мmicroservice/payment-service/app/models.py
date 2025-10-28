from sqlalchemy import Column, Integer, String, DateTime, Float
from .database import Base

class Payment(Base):
    __tablename__ = "payments"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    user_id = Column(Integer)
    amount = Column(Float)
    status = Column(String)
    payment_method = Column(String)
    transaction_id = Column(String)
    created_at = Column(DateTime)