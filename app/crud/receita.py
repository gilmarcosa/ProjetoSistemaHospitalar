from sqlalchemy.orm import Session
from app.models.receita import Receita
from app.schemas.receita import ReceitaCreate, ReceitaUpdate


def get_receita(db: Session, receita_id: int):
    return db.query(Receita).filter(Receita.id == receita_id).first()


def get_receitas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Receita).offset(skip).limit(limit).all()


def create_receita(db: Session, receita: ReceitaCreate):
    db_receita = Receita(**receita.dict())
    db.add(db_receita)
    db.commit()
    db.refresh(db_receita)
    return db_receita


def update_receita(db: Session, receita_id: int, receita_update: ReceitaUpdate):
    db_receita = get_receita(db, receita_id)
    if not db_receita:
        return None
    for key, value in receita_update.dict(exclude_unset=True).items():
        setattr(db_receita, key, value)
    db.commit()
    db.refresh(db_receita)
    return db_receita


def delete_receita(db: Session, receita_id: int):
    db_receita = get_receita(db, receita_id)
    if not db_receita:
        return None
    db.delete(db_receita)
    db.commit()
    return db_receita
