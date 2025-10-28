from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, schemas

router = APIRouter()

@router.post("/")
def create_user(user: dict, db: Session = Depends(database.get_db)):
    db_user = models.User(
        email=user.get("email"),
        hashed_password="hashed_password",
        full_name=user.get("full_name"),
        phone=user.get("phone")
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/")
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users