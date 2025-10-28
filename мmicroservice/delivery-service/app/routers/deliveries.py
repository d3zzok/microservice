from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, schemas
import uuid
from datetime import datetime, timedelta

router = APIRouter()

@router.post("/", response_model=schemas.DeliveryResponse)
def create_delivery(delivery: schemas.DeliveryCreate, db: Session = Depends(database.get_db)):
    # Создание записи о доставке
    db_delivery = models.Delivery(
        order_id=delivery.order_id,
        user_id=delivery.user_id,
        address=delivery.address,
        status="preparing",
        tracking_number=f"TRK{delivery.order_id:08d}",
        estimated_delivery=datetime.utcnow() + timedelta(days=3)
    )
    
    db.add(db_delivery)
    db.commit()
    db.refresh(db_delivery)
    
    return db_delivery

@router.get("/{delivery_id}", response_model=schemas.DeliveryResponse)
def get_delivery(delivery_id: int, db: Session = Depends(database.get_db)):
    delivery = db.query(models.Delivery).filter(models.Delivery.id == delivery_id).first()
    if delivery is None:
        raise HTTPException(status_code=404, detail="Delivery not found")
    return delivery