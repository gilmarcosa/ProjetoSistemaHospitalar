from sqlalchemy.orm import Session
from app.models.internacao import Internacao
from app.schemas.internacao import InternacaoCreate

def create_internacao(db: Session, internacao: InternacaoCreate):
    db_internacao = Internacao(**internacao.model_dump())
    db.add(db_internacao)
    db.commit()
    db.refresh(db_internacao)
    return db_internacao

def get_internacoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Internacao).offset(skip).limit(limit).all()

def get_internacao(db: Session, internacao_id: int):
    return db.query(Internacao).filter(Internacao.id == internacao_id).first()

def update_internacao(db: Session, internacao_id: int, internacao: InternacaoCreate):
    db_internacao = db.query(Internacao).filter(Internacao.id == internacao_id).first()
    if db_internacao:
        for key, value in internacao.model_dump().items():
            setattr(db_internacao, key, value)
        db.commit()
        db.refresh(db_internacao)
    return db_internacao

def delete_internacao(db: Session, internacao_id: int):
    db_internacao = db.query(Internacao).filter(Internacao.id == internacao_id).first()
    if db_internacao:
        db.delete(db_internacao)
        db.commit()
    return db_internacao
