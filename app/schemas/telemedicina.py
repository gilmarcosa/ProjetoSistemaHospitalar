from pydantic import BaseModel
from datetime import datetime

class TelemedicinaBase(BaseModel):
    paciente_id: int
    profissional_id: int
    status: str = "Aguardando"
    horario: datetime = datetime.utcnow()
    link_acesso: str | None = None

class TelemedicinaCreate(TelemedicinaBase):
    pass

class TelemedicinaRead(TelemedicinaBase):
    id: int

    class Config:
        from_attributes = True
