from sqlalchemy.orm import Session
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate
from app.core.security import hash_senha

def criar_usuario(db: Session, usuario: UsuarioCreate):
    db_usuario = Usuario(email=usuario.email, senha_hash=hash_senha(usuario.senha))
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

def buscar_por_email(db: Session, email: str):
    return db.query(Usuario).filter(Usuario.email == email).first()
