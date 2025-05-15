from pydantic import BaseModel
from datetime import time
from typing import Optional


class ConsultaBase(BaseModel):
    paciente_id: int
    profissional_id: int
    status: Optional[str] = "Agendada"
    hora: time

class ConsultaCreate(ConsultaBase):
    pass

class ConsultaUpdate(BaseModel):
    status: Optional[str] = None
    hora: Optional[time] = None
    paciente_id: Optional[int] = None
    profissional_id: Optional[int] = None


class ConsultaRead(ConsultaBase):
    id: int

    class Config:
        from_attributes = True
