from sqlalchemy.orm import Session
from app.models.telemedicina import Telemedicina
from app.schemas.telemedicina import TelemedicinaCreate

def criar_telemedicina(db: Session, telemedicina: TelemedicinaCreate):
    nova_telemedicina = Telemedicina(**telemedicina.dict())
    db.add(nova_telemedicina)
    db.commit()
    db.refresh(nova_telemedicina)
    return nova_telemedicina

def listar_telemedicinas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Telemedicina).offset(skip).limit(limit).all()

def obter_telemedicina(db: Session, telemedicina_id: int):
    return db.query(Telemedicina).filter(Telemedicina.id == telemedicina_id).first()

def deletar_telemedicina(db: Session, telemedicina_id: int):
    telemedicina = obter_telemedicina(db, telemedicina_id)
    if telemedicina:
        db.delete(telemedicina)
        db.commit()
    return telemedicina

def atualizar_telemedicina(db: Session, telemedicina_id: int, dados: TelemedicinaCreate):
    telemedicina = obter_telemedicina(db, telemedicina_id)
    if telemedicina:
        for key, value in dados.dict().items():
            setattr(telemedicina, key, value)
        db.commit()
        db.refresh(telemedicina)
    return telemedicina
