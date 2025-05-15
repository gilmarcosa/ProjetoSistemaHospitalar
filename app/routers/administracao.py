from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.schemas.administracao import AdministracaoCreate, AdministracaoRead
from app.crud import administracao as crud_administracao

router = APIRouter(prefix="/administracoes", tags=["Administracoes"])

@router.post("/", response_model=AdministracaoRead)
def create_administracao(administracao: AdministracaoCreate, db: Session = Depends(get_db)):
    return crud_administracao.create_administracao(db, administracao)

@router.get("/", response_model=List[AdministracaoRead])
def read_administracoes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_administracao.get_administracoes(db, skip=skip, limit=limit)

@router.get("/{administracao_id}", response_model=AdministracaoRead)
def read_administracao(administracao_id: int, db: Session = Depends(get_db)):
    db_administracao = crud_administracao.get_administracao(db, administracao_id)
    if not db_administracao:
        raise HTTPException(status_code=404, detail="Administracao não encontrada")
    return db_administracao

@router.put("/{administracao_id}", response_model=AdministracaoRead)
def update_administracao(administracao_id: int, administracao: AdministracaoCreate, db: Session = Depends(get_db)):
    db_administracao = crud_administracao.update_administracao(db, administracao_id, administracao)
    if not db_administracao:
        raise HTTPException(status_code=404, detail="Administracao não encontrada")
    return db_administracao

@router.delete("/{administracao_id}")
def delete_administracao(administracao_id: int, db: Session = Depends(get_db)):
    db_administracao = crud_administracao.delete_administracao(db, administracao_id)
    if not db_administracao:
        raise HTTPException(status_code=404, detail="Administracao não encontrada")
    return {"ok": True}
