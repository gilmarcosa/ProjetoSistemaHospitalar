from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas import paciente as schemas
from app.crud import paciente as crud_paciente

router = APIRouter(prefix="/pacientes", tags=["Pacientes"])

@router.post("/", response_model=schemas.PacienteRead)
def create_paciente(paciente: schemas.PacienteCreate, db: Session = Depends(get_db)):
    return crud.paciente.create_paciente(db, paciente)

@router.get("/{paciente_id}", response_model=schemas.PacienteRead)
def read_paciente(paciente_id: int, db: Session = Depends(get_db)):
    db_paciente = crud.paciente.get_paciente(db, paciente_id)
    if not db_paciente:
        raise HTTPException(status_code=404, detail="Paciente não encontrado")
    return db_paciente

@router.get("/", response_model=list[schemas.PacienteRead])
def read_pacientes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.paciente.get_pacientes(db, skip, limit)

@router.put("/{paciente_id}", response_model=schemas.PacienteRead)
def update_paciente(paciente_id: int, paciente: schemas.PacienteUpdate, db: Session = Depends(get_db)):
    return crud.paciente.update_paciente(db, paciente_id, paciente)

@router.delete("/{paciente_id}", response_model=schemas.PacienteRead)
def delete_paciente(paciente_id: int, db: Session = Depends(get_db)):
    return crud.paciente.delete_paciente(db, paciente_id)
