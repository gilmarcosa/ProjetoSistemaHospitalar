from pydantic import BaseModel

class ProfissionalInternacaoBase(BaseModel):
    profissional_id: int
    internacao_id: int

class ProfissionalInternacaoCreate(ProfissionalInternacaoBase):
    pass

class ProfissionalInternacaoResponse(ProfissionalInternacaoBase):
    id: int

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2

