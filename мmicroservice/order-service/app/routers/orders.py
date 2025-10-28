from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database

router = APIRouter()

@router.post("/")
def create_order(order: dict, db: Session = Depends(database.get_db)):
    db_order = models.Order(
        user_id=order.get("user_id"),
        status="created",
        total_amount=order.get("total_amount"),
        items=order.get("items"),
        shipping_address=order.get("shipping_address")
    )
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

@router.get("/")
def get_orders(db: Session = Depends(database.get_db)):
    orders = db.query(models.Order).all()
    return orders