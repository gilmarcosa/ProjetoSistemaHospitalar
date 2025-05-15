from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.profissionalInternacao import ProfissionalInternacaoCreate, ProfissionalInternacaoResponse
from app.crud import profissionalInternacao as crud
from app.database import get_db

router = APIRouter(prefix="/profissional-internacao", tags=["ProfissionalInternacao"])

@router.post("/", response_model=ProfissionalInternacaoResponse)
def create(data: ProfissionalInternacaoCreate, db: Session = Depends(get_db)):
    return crud.create_profissional_internacao(db, data)

@router.get("/{id}", response_model=ProfissionalInternacaoResponse)
def read(id: int, db: Session = Depends(get_db)):
    result = crud.get_profissional_internacao(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return result

@router.get("/", response_model=list[ProfissionalInternacaoResponse])
def read_all(db: Session = Depends(get_db)):
    return crud.get_all_profissional_internacoes(db)

@router.delete("/{id}", response_model=ProfissionalInternacaoResponse)
def delete(id: int, db: Session = Depends(get_db)):
    result = crud.delete_profissional_internacao(db, id)
    if not result:
        raise HTTPException(status_code=404, detail="Não encontrado")
    return result
