from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Paciente(Base):
    __tablename__ = "paciente"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    data_nascimento = Column(Date, nullable=False)
    historico_clinico = Column(String, nullable=True)
    administracao_id = Column(Integer, ForeignKey("administracao.id"), nullable=True)

    # Relacionamentos (Adicionaremos depois)


    internacoes = relationship("Internacao", back_populates="paciente", lazy="joined")

    administrador = relationship("Administracao", back_populates="pacientes")


Paciente.consultas = relationship("Consulta", back_populates="paciente")
Paciente.telemedicinas = relationship("Telemedicina", back_populates="paciente")
Paciente.receitas = relationship("Receita", back_populates="paciente", lazy="joined")
Paciente.prontuarios = relationship("Prontuario", back_populates="paciente")