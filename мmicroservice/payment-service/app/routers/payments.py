from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, schemas
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/", response_model=schemas.PaymentResponse)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(database.get_db)):
    # Имитация обработки платежа
    db_payment = models.Payment(
        order_id=payment.order_id,
        user_id=payment.user_id,
        amount=payment.amount,
        status="completed",  # В реальности здесь была бы логика обработки
        payment_method="credit_card",
        transaction_id=str(uuid.uuid4()),
        created_at=datetime.utcnow()
    )
    
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    
    return db_payment

@router.get("/{payment_id}", response_model=schemas.PaymentResponse)
def get_payment(payment_id: int, db: Session = Depends(database.get_db)):
    payment = db.query(models.Payment).filter(models.Payment.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment