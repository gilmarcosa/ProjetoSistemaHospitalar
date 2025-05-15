from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.schemas.leito import LeitoCreate, LeitoRead
from app.crud import leito as crud_leito
from app.database import get_db

router = APIRouter(prefix="/leitos", tags=["Leitos"])

@router.post("/", response_model=LeitoRead)
def create(leito: LeitoCreate, db: Session = Depends(get_db)):
    return crud_leito.create_leito(db, leito)

@router.get("/", response_model=List[LeitoRead])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud_leito.get_leitos(db, skip, limit)

@router.get("/{leito_id}", response_model=LeitoRead)
def read_one(leito_id: int, db: Session = Depends(get_db)):
    leito = crud_leito.get_leito(db, leito_id)
    if not leito:
        raise HTTPException(status_code=404, detail="Leito não encontrado")
    return leito

@router.put("/{leito_id}", response_model=LeitoRead)
def update(leito_id: int, leito: LeitoCreate, db: Session = Depends(get_db)):
    updated = crud_leito.update_leito(db, leito_id, leito)
    if not updated:
        raise HTTPException(status_code=404, detail="Leito não encontrado")
    return updated

@router.delete("/{leito_id}")
def delete(leito_id: int, db: Session = Depends(get_db)):
    deleted = crud_leito.delete_leito(db, leito_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Leito não encontrado")
    return {"ok": True}
