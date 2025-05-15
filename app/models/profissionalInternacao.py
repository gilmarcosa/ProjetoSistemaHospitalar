# models/profissional_internacao.py

from sqlalchemy import Column, Integer, ForeignKey
from app.database import Base

class ProfissionalInternacao(Base):
    __tablename__ = "profissional_internacao"

    id = Column(Integer, primary_key=True, index=True)
    profissional_id = Column(Integer, ForeignKey("profissional_saude.id"), nullable=False)
    internacao_id = Column(Integer, ForeignKey("internacao.id"), nullable=False)
