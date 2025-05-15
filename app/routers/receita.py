from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import receita as crud_receita
from app.schemas import receita as schemas

router = APIRouter(prefix="/receitas", tags=["Receitas"])

@router.post("/", response_model=schemas.ReceitaRead)
def create_receita(receita: schemas.ReceitaCreate, db: Session = Depends(get_db)):
    return crud_receita.create_receita(db, receita)

@router.get("/{receita_id}", response_model=schemas.ReceitaRead)
def read_receita(receita_id: int, db: Session = Depends(get_db)):
    db_receita = crud_receita.get_receita(db, receita_id)
    if not db_receita:
        raise HTTPException(status_code=404, detail="Receita não encontrada")
    return db_receita

@router.get("/", response_model=list[schemas.ReceitaRead])
def read_receitas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_receita.get_receitas(db, skip, limit)

@router.put("/{receita_id}", response_model=schemas.ReceitaRead)
def update_receita(receita_id: int, receita: schemas.ReceitaUpdate, db: Session = Depends(get_db)):
    return crud_receita.update_receita(db, receita_id, receita)

@router.delete("/{receita_id}", response_model=schemas.ReceitaRead)
def delete_receita(receita_id: int, db: Session = Depends(get_db)):
    return crud_receita.delete_receita(db, receita_id)
