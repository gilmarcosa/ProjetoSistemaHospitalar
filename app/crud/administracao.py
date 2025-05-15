from sqlalchemy.orm import Session
from app.models.administracao import Administracao
from app.schemas.administracao import AdministracaoCreate

def create_administracao(db: Session, administracao: AdministracaoCreate):

    db_administracao = Administracao(**administracao.model_dump())
    db.add(db_administracao)
    db.commit()
    db.refresh(db_administracao)
    return db_administracao

def get_administracoes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Administracao).offset(skip).limit(limit).all()

def get_administracao(db: Session, administracao_id: int):
    return db.query(Administracao).filter(Administracao.id == administracao_id).first()

def update_administracao(db: Session, administracao_id: int, administracao: AdministracaoCreate):
    db_administracao = db.query(Administracao).filter(Administracao.id == administracao_id).first()
    if db_administracao:
        for key, value in administracao.model_dump().items():
            setattr(db_administracao, key, value)
        db.commit()
        db.refresh(db_administracao)
    return db_administracao

def delete_administracao(db: Session, administracao_id: int):
    db_administracao = db.query(Administracao).filter(Administracao.id == administracao_id).first()
    if db_administracao:
        db.delete(db_administracao)
        db.commit()
    return db_administracao
