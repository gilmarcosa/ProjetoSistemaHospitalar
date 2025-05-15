from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.database import Base



class Internacao(Base):
    __tablename__ = "internacao"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissional_saude.id"))
    leito_id = Column(Integer, ForeignKey("leito.id"), nullable=False)
    administracao_id = Column(Integer, ForeignKey("administracao.id"), nullable=True)  # Adicionando a chave estrangeira
    data_entrada = Column(Date, nullable=False)
    data_saida = Column(Date, nullable=True)
    status = Column(String, default="Ativo")

    profissionais = relationship("ProfissionalSaude", secondary="profissional_internacao", back_populates="internacoes")
    paciente = relationship("Paciente", back_populates="internacoes")
    leito = relationship("Leito", back_populates="internacoes")

Internacao.administrador = relationship("Administracao", back_populates="internacoes")

