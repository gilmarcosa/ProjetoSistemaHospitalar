from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.models.prontuario import Prontuario

from app.database import Base

class Receita(Base):
    __tablename__ = "receita"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    profissional_id = Column(Integer, ForeignKey("profissional_saude.id"))
    prontuario_id = Column(Integer, ForeignKey("prontuario.id"), nullable=False)
    medicamento = Column(String, unique=True, nullable=False)
    observacoes = Column(String, nullable=False)
    dosagem = Column(String, nullable=False)
    validade = Column(Date, nullable=False)

    paciente = relationship("Paciente", back_populates="receitas")
    profissional = relationship("ProfissionalSaude", back_populates="receitas")
    prontuario = relationship("Prontuario", back_populates="receitas")