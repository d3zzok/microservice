from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime

class UserBase(BaseModel):
    email: str
    full_name: str
    phone: str

class UserCreate(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class OrderCreate(BaseModel):
    user_id: int
    shipping_address: Dict[str, Any]
    items: List[Dict[str, Any]]

class OrderResponse(BaseModel):
    id: int
    user_id: int
    status: str
    total_amount: float
    created_at: datetime
    items: List[Dict[str, Any]]
    shipping_address: Dict[str, Any]
    
    class Config:
        from_attributes = True