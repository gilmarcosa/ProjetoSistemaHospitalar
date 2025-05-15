from pydantic import BaseModel
from typing import Optional
from datetime import date

class InternacaoBase(BaseModel):
    paciente_id: int
    leito_id: int
    data_entrada: date
    data_saida: Optional[date] = None
    status: Optional[str] = "Ativo"
    profissional_id: Optional[int] = None
    administracao_id: Optional[int] = None

class InternacaoCreate(InternacaoBase):
    pass

class InternacaoRead(InternacaoBase):
    id: int

    class Config:
        from_attributes = True
