from pydantic import BaseModel
from typing import Optional

class AdministracaoBase(BaseModel):
    nome: str
    cargo: Optional[str] = None

class AdministracaoCreate(AdministracaoBase):
    pass

class AdministracaoRead(AdministracaoBase):
    id: int

    class Config:
        from_attributes = True
