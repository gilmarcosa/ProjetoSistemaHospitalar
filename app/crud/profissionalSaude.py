from sqlalchemy.orm import Session
from app.models.profissionalSaude import ProfissionalSaude
from app.schemas.profissionalSaude import ProfissionalSaudeCreate, ProfissionalSaudeUpdate

def get_profissional(db: Session, profissional_id: int):
    return db.query(ProfissionalSaude).filter(ProfissionalSaude.id == profissional_id).first()

def get_profissionais(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ProfissionalSaude).offset(skip).limit(limit).all()

def create_profissional(db: Session, profissional: ProfissionalSaudeCreate):
    db_profissional = ProfissionalSaude(**profissional.dict())
    db.add(db_profissional)
    db.commit()
    db.refresh(db_profissional)
    return db_profissional

def update_profissional(db: Session, profissional_id: int, profissional_update: ProfissionalSaudeUpdate):
    profissional = get_profissional(db, profissional_id)
    if not profissional:
        return None
    for key, value in profissional_update.dict(exclude_unset=True).items():
        setattr(profissional, key, value)
    db.commit()
    db.refresh(profissional)
    return profissional

def delete_profissional(db: Session, profissional_id: int):
    profissional = get_profissional(db, profissional_id)
    if not profissional:
        return None
    db.delete(profissional)
    db.commit()
    return profissional
