from sqlalchemy import Column, Integer, String, DateTime, JSON
from .database import Base

class Delivery(Base):
    __tablename__ = "deliveries"
    
    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer)
    user_id = Column(Integer)
    address = Column(JSON)
    status = Column(String)
    tracking_number = Column(String)
    estimated_delivery = Column(DateTime)
    actual_delivery = Column(DateTime)