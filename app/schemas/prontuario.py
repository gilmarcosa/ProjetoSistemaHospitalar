from typing import Optional

from pydantic import BaseModel
from datetime import date

class ProntuarioBase(BaseModel):
    paciente_id: int
    profissional_id: int
    receita: str
    diagnostico: str
    observacoes: str

class ProntuarioCreate(ProntuarioBase):
    pass

class ProntuarioUpdate(BaseModel):
    paciente_id: Optional[int] = None
    profissional_id: Optional[int] = None
    receita: Optional[str] = None
    diagnostico: Optional[str] = None
    observacoes: Optional[str] = None

class ProntuarioRead(ProntuarioBase):
    id: int

    class Config:
        from_attributes = True
