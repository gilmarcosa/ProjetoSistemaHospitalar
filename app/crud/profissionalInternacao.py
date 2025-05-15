from sqlalchemy.orm import Session
from app.models.profissionalInternacao import ProfissionalInternacao
from app.schemas.profissionalInternacao import ProfissionalInternacaoCreate



def create_profissional_internacao(db: Session, data: ProfissionalInternacaoCreate):
    novo = ProfissionalInternacao(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def get_profissional_internacao(db: Session, id: int):
    return db.query(ProfissionalInternacao).filter(ProfissionalInternacao.id == id).first()

def get_all_profissional_internacoes(db: Session):
    return db.query(ProfissionalInternacao).all()

def delete_profissional_internacao(db: Session, id: int):
    obj = db.query(ProfissionalInternacao).filter(ProfissionalInternacao.id == id).first()
    if obj:
        db.delete(obj)
        db.commit()
    return obj
