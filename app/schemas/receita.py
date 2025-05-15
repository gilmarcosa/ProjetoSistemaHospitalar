from pydantic import BaseModel
from typing import Optional
from datetime import date


class ReceitaBase(BaseModel):
    paciente_id: int
    profissional_id: int
    observacoes: str
    medicamento: str
    validade: date
    prontuario_id: int
    dosagem: str


class ReceitaCreate(ReceitaBase):
    pass


class ReceitaUpdate(BaseModel):
    observacoes: Optional[str] = None
    medicamento: Optional[str] = None
    paciente_id: Optional[int] = None
    profissional_id: Optional[int] = None
    validade:Optional [date] = None
    prontuario_id:Optional [int] = None
    dosagem: Optional [str] = None


class ReceitaRead(ReceitaBase):
    id: int

    class Config:
        from_attributes = True

