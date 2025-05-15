from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.telemedicina import TelemedicinaCreate, TelemedicinaRead
from app.crud import telemedicina as crud_telemedicina
from app.database import get_db
from typing import List

router = APIRouter(prefix="/telemedicina", tags=["Telemedicina"])

@router.post("/", response_model=TelemedicinaRead)
def criar(telemedicina: TelemedicinaCreate, db: Session = Depends(get_db)):
    return crud_telemedicina.criar_telemedicina(db, telemedicina)

@router.get("/", response_model=List[TelemedicinaRead])
def listar(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_telemedicina.listar_telemedicinas(db, skip, limit)

@router.get("/{telemedicina_id}", response_model=TelemedicinaRead)
def obter(telemedicina_id: int, db: Session = Depends(get_db)):
    telemedicina = crud_telemedicina.obter_telemedicina(db, telemedicina_id)
    if not telemedicina:
        raise HTTPException(status_code=404, detail="Telemedicina não encontrada")
    return telemedicina

@router.delete("/{telemedicina_id}", response_model=TelemedicinaRead)
def deletar(telemedicina_id: int, db: Session = Depends(get_db)):
    telemedicina = crud_telemedicina.deletar_telemedicina(db, telemedicina_id)
    if not telemedicina:
        raise HTTPException(status_code=404, detail="Telemedicina não encontrada")
    return telemedicina

@router.put("/{telemedicina_id}", response_model=TelemedicinaRead)
def atualizar(telemedicina_id: int, dados: TelemedicinaCreate, db: Session = Depends(get_db)):
    telemedicina = crud_telemedicina.atualizar_telemedicina(db, telemedicina_id, dados)
    if not telemedicina:
        raise HTTPException(status_code=404, detail="Telemedicina não encontrada")
    return telemedicina
