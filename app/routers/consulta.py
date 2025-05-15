from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.crud import consulta as crud_consulta
from app.schemas import consulta as schemas

router = APIRouter(prefix="/consultas", tags=["Consultas"])

@router.post("/", response_model=schemas.ConsultaRead)
def create_consulta(consulta: schemas.ConsultaCreate, db: Session = Depends(get_db)):
    return crud_consulta.create_consulta(db, consulta)

@router.get("/{consulta_id}", response_model=schemas.ConsultaRead)
def read_consulta(consulta_id: int, db: Session = Depends(get_db)):
    db_consulta = crud_consulta.get_consulta(db, consulta_id)
    if not db_consulta:
        raise HTTPException(status_code=404, detail="Consulta não encontrada")
    return db_consulta

@router.get("/", response_model=list[schemas.ConsultaRead])
def read_consultas(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_consulta.get_consultas(db, skip, limit)

@router.put("/{consulta_id}", response_model=schemas.ConsultaRead)
def update_consulta(consulta_id: int, consulta: schemas.ConsultaUpdate, db: Session = Depends(get_db)):
    return crud_consulta.update_consulta(db, consulta_id, consulta)

@router.delete("/{consulta_id}", response_model=schemas.ConsultaRead)
def delete_consulta(consulta_id: int, db: Session = Depends(get_db)):
    return crud_consulta.delete_consulta(db, consulta_id)
