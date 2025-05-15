from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import prontuario as schemas
from app.crud import prontuario as crud_prontuario

router = APIRouter(prefix="/prontuarios", tags=["Prontuarios"])

@router.post("/", response_model=schemas.ProntuarioRead)
def create_prontuario(prontuario: schemas.ProntuarioCreate, db: Session = Depends(get_db)):
    return crud_prontuario.create_prontuario(db, prontuario)

@router.get("/{prontuario_id}", response_model=schemas.ProntuarioRead)
def read_prontuario(prontuario_id: int, db: Session = Depends(get_db)):
    prontuario = crud_prontuario.get_prontuario(db, prontuario_id)
    if not prontuario:
        raise HTTPException(status_code=404, detail="Prontuário não encontrado")
    return prontuario

@router.get("/", response_model=list[schemas.ProntuarioRead])
def read_prontuarios(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_prontuario.get_prontuarios(db, skip, limit)

@router.put("/{prontuario_id}", response_model=schemas.ProntuarioRead)
def update_prontuario(prontuario_id: int, prontuario: schemas.ProntuarioUpdate, db: Session = Depends(get_db)):
    return crud_prontuario.update_prontuario(db, prontuario_id, prontuario)

@router.delete("/{prontuario_id}", response_model=schemas.ProntuarioRead)
def delete_prontuario(prontuario_id: int, db: Session = Depends(get_db)):
    return crud_prontuario.delete_prontuario(db, prontuario_id)
