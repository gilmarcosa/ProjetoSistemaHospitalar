from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base

class Administracao(Base):
        __tablename__ = "administracao"

        id = Column(Integer, primary_key=True, index=True)
        nome = Column(String, nullable=False)
        cargo = Column(String)


        pacientes = relationship("Paciente", back_populates="administrador")
        internacoes = relationship("Internacao", back_populates="administrador")