from sqlalchemy.orm import Session
from app.models.prontuario import Prontuario
from app.schemas.prontuario import ProntuarioCreate, ProntuarioUpdate

def get_prontuario(db: Session, prontuario_id: int):
    return db.query(Prontuario).filter(Prontuario.id == prontuario_id).first()

def get_prontuarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Prontuario).offset(skip).limit(limit).all()

def create_prontuario(db: Session, prontuario: ProntuarioCreate):
    db_prontuario = Prontuario(**prontuario.dict())
    db.add(db_prontuario)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario

def update_prontuario(db: Session, prontuario_id: int, prontuario_update: ProntuarioUpdate):
    db_prontuario = get_prontuario(db, prontuario_id)
    if not db_prontuario:
        return None
    for key, value in prontuario_update.dict(exclude_unset=True).items():
        setattr(db_prontuario, key, value)
    db.commit()
    db.refresh(db_prontuario)
    return db_prontuario

def delete_prontuario(db: Session, prontuario_id: int):
    db_prontuario = get_prontuario(db, prontuario_id)
    if not db_prontuario:
        return None
    db.delete(db_prontuario)
    db.commit()
    return db_prontuario
