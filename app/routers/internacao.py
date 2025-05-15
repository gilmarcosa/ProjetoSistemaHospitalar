from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.internacao import InternacaoCreate, InternacaoRead
from app.crud import internacao as crud_internacao

router = APIRouter(prefix="/internacoes", tags=["Internacoes"])

@router.post("/", response_model=InternacaoRead)
def create_internacao(internacao: InternacaoCreate, db: Session = Depends(get_db)):
    return crud_internacao.create_internacao(db, internacao)

@router.get("/", response_model=List[InternacaoRead])
def read_internacoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_internacao.get_internacoes(db, skip=skip, limit=limit)

@router.get("/{internacao_id}", response_model=InternacaoRead)
def read_internacao(internacao_id: int, db: Session = Depends(get_db)):
    db_internacao = crud_internacao.get_internacao(db, internacao_id)
    if not db_internacao:
        raise HTTPException(status_code=404, detail="Internação não encontrada")
    return db_internacao

@router.put("/{internacao_id}", response_model=InternacaoRead)
def update_internacao(internacao_id: int, internacao: InternacaoCreate, db: Session = Depends(get_db)):
    db_internacao = crud_internacao.update_internacao(db, internacao_id, internacao)
    if not db_internacao:
        raise HTTPException(status_code=404, detail="Internação não encontrada")
    return db_internacao

@router.delete("/{internacao_id}")
def delete_internacao(internacao_id: int, db: Session = Depends(get_db)):
    db_internacao = crud_internacao.delete_internacao(db, internacao_id)
    if not db_internacao:
        raise HTTPException(status_code=404, detail="Internação não encontrada")
    return {"ok": True}
