from sqlalchemy import Column, Integer, String, Time, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Consulta(Base):
    __tablename__ = "consulta"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"))
    profissional_id = Column(Integer, ForeignKey("profissional_saude.id"))
    status = Column(String)
    hora = Column(Time)


    profissional_saude = relationship("ProfissionalSaude", back_populates="consultas")

Consulta.paciente = relationship("Paciente", back_populates="consultas")