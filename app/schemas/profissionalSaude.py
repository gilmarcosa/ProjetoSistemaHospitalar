from pydantic import BaseModel
from typing import Optional

class ProfissionalSaudeBase(BaseModel):
    nome: str
    especialidade: Optional[str] = None

class ProfissionalSaudeCreate(ProfissionalSaudeBase):
    pass

class ProfissionalSaudeUpdate(BaseModel):
    nome: Optional[str] = None
    especialidade: Optional[str] = None

class ProfissionalSaudeRead(ProfissionalSaudeBase):
    id: int

    class Config:
        from_attributes = True

