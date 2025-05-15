from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.schemas.paciente import PacienteCreate, PacienteUpdate

def get_paciente(db: Session, paciente_id: int):
    return db.query(Paciente).filter(Paciente.id == paciente_id).first()

def get_pacientes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Paciente).offset(skip).limit(limit).all()

def create_paciente(db: Session, paciente: PacienteCreate):
    db_paciente = Paciente(**paciente.dict())
    db.add(db_paciente)
    db.commit()
    db.refresh(db_paciente)
    return db_paciente

def update_paciente(db: Session, paciente_id: int, paciente_update: PacienteUpdate):
    paciente = get_paciente(db, paciente_id)
    if not paciente:
        return None
    for key, value in paciente_update.dict(exclude_unset=True).items():
        setattr(paciente, key, value)
    db.commit()
    db.refresh(paciente)
    return paciente

def delete_paciente(db: Session, paciente_id: int):
    paciente = get_paciente(db, paciente_id)
    if not paciente:
        return None
    db.delete(paciente)
    db.commit()
    return paciente
