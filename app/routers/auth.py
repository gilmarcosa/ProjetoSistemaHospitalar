from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.usuario import UsuarioCreate, UsuarioRead, UsuarioLogin
from app.database import get_db
from app.crud import usuario as crud_usuario
from app.core.security import verificar_senha, criar_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/register", response_model=UsuarioRead)
def register(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    db_usuario = crud_usuario.buscar_por_email(db, usuario.email)
    if db_usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud_usuario.criar_usuario(db, usuario)

@router.post("/login")
def login(usuario: UsuarioLogin, db: Session = Depends(get_db)):
    db_usuario = crud_usuario.buscar_por_email(db, usuario.email)
    if not db_usuario or not verificar_senha(usuario.senha, db_usuario.senha_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    token = criar_token({"sub": db_usuario.email})
    return {"access_token": token, "token_type": "bearer"}
