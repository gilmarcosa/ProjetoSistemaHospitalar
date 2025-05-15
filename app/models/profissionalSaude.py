from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.profissionalInternacao import ProfissionalInternacao

class ProfissionalSaude(Base):
    __tablename__ = "profissional_saude"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    nome = Column(String, nullable=False)
    especialidade = Column(String)


    consultas = relationship("Consulta", back_populates="profissional_saude")
    receitas = relationship("Receita", back_populates="profissional")
    prontuarios = relationship("Prontuario", back_populates="profissional")
    telemedicinas = relationship("Telemedicina", back_populates="profissional")
    internacoes = relationship("Internacao", secondary="profissional_internacao", back_populates="profissionais")
