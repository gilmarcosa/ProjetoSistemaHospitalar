from pydantic import BaseModel

class LeitoBase(BaseModel):
    numero: int
    tipo: str
    status: bool = True

class LeitoCreate(LeitoBase):
    pass

class LeitoRead(LeitoBase):
    id: int

    class Config:
        from_attributes = True
