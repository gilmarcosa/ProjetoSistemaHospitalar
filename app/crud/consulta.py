from sqlalchemy.orm import Session
from app.models.consulta import Consulta
from app.schemas.consulta import ConsultaCreate, ConsultaUpdate


def get_consulta(db: Session, consulta_id: int):
    return db.query(Consulta).filter(Consulta.id == consulta_id).first()


def get_consultas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Consulta).offset(skip).limit(limit).all()


def create_consulta(db: Session, consulta: ConsultaCreate):
    db_consulta = Consulta(**consulta.dict())
    db.add(db_consulta)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta


def update_consulta(db: Session, consulta_id: int, consulta_update: ConsultaUpdate):
    db_consulta = get_consulta(db, consulta_id)
    if not db_consulta:
        return None
    for key, value in consulta_update.dict(exclude_unset=True).items():
        setattr(db_consulta, key, value)
    db.commit()
    db.refresh(db_consulta)
    return db_consulta


def delete_consulta(db: Session, consulta_id: int):
    db_consulta = get_consulta(db, consulta_id)
    if not db_consulta:
        return None
    db.delete(db_consulta)
    db.commit()
    return db_consulta
