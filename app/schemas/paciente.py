from pydantic import BaseModel
from datetime import date
from typing import Optional

# Atributos comuns para leitura e criação
class PacienteBase(BaseModel):
    nome: str
    data_nascimento: date
    historico_clinico: Optional[str] = None

# Usado quando você for CRIAR um paciente (POST)
class PacienteCreate(PacienteBase):
    pass

class PacienteUpdate(BaseModel):
    nome: Optional[str] = None
    data_nascimento: Optional[date] = None
    historico_clinico: Optional[str] = None

# Usado para RESPONDER com os dados de um paciente (GET)
class PacienteRead(PacienteBase):
    id: int

    class Config:
        from_attributes = True
