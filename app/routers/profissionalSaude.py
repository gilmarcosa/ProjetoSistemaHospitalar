from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app import crud
from app.schemas import profissionalSaude as schemas
from app.crud import profissionalSaude as crud_profissional

router = APIRouter(prefix="/profissionais", tags=["Profissionais de Saúde"])

@router.post("/", response_model=schemas.ProfissionalSaudeRead)
def create_profissional(profissional: schemas.ProfissionalSaudeCreate, db: Session = Depends(get_db)):
    return crud.profissionalSaude.create_profissional(db, profissional)

@router.get("/{profissional_id}", response_model=schemas.ProfissionalSaudeRead)
def read_profissional(profissional_id: int, db: Session = Depends(get_db)):
    db_profissional = crud.profissionalSaude.get_profissional(db, profissional_id)
    if not db_profissional:
        raise HTTPException(status_code=404, detail="Profissional não encontrado")
    return db_profissional

@router.get("/", response_model=list[schemas.ProfissionalSaudeRead])
def read_profissionais(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.profissionalSaude.get_profissionais(db, skip, limit)

@router.put("/{profissional_id}", response_model=schemas.ProfissionalSaudeRead)
def update_profissional(profissional_id: int, profissional: schemas.ProfissionalSaudeUpdate, db: Session = Depends(get_db)):
    return crud.profissionalSaude.update_profissional(db, profissional_id, profissional)

@router.delete("/{profissional_id}", response_model=schemas.ProfissionalSaudeRead)
def delete_profissional(profissional_id: int, db: Session = Depends(get_db)):
    return crud.profissionalSaude.delete_profissional(db, profissional_id)