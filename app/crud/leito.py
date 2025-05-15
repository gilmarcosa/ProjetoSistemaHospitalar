# app/crud/leito.py

from sqlalchemy.orm import Session
from app.models.leito import Leito
from app.schemas.leito import LeitoCreate

def create_leito(db: Session, leito: LeitoCreate):
    db_leito = Leito(**leito.model_dump())
    db.add(db_leito)
    db.commit()
    db.refresh(db_leito)
    return db_leito

def get_leito(db: Session, leito_id: int):
    return db.query(Leito).filter(Leito.id == leito_id).first()

def get_leitos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Leito).offset(skip).limit(limit).all()

def update_leito(db: Session, leito_id: int, leito: LeitoCreate):
    db_leito = db.query(Leito).filter(Leito.id == leito_id).first()
    if db_leito:
        for key, value in leito.model_dump().items():
            setattr(db_leito, key, value)
        db.commit()
        db.refresh(db_leito)
    return db_leito

def delete_leito(db: Session, leito_id: int):
    db_leito = db.query(Leito).filter(Leito.id == leito_id).first()
    if db_leito:
        db.delete(db_leito)
        db.commit()
    return db_leito
