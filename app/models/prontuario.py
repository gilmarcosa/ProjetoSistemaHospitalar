from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base

class Prontuario(Base):
    __tablename__ = "prontuario"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissional_saude.id"), nullable=False)
    receita = Column(String, nullable=True)
    diagnostico = Column(String, unique=True, nullable=False)
    observacoes = Column(String, nullable=False)

    paciente = relationship("Paciente", back_populates="prontuarios")
    profissional = relationship("ProfissionalSaude", back_populates="prontuarios")
    receitas = relationship("Receita", back_populates="prontuario")
