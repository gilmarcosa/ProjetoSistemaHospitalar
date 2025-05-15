from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class Telemedicina(Base):
    __tablename__ = "telemedicina"

    id = Column(Integer, primary_key=True, index=True)
    paciente_id = Column(Integer, ForeignKey("paciente.id"), nullable=False)
    profissional_id = Column(Integer, ForeignKey("profissional_saude.id"), nullable=False)
    status = Column(String, nullable=False, default="Aguardando")
    horario = Column(DateTime, default=datetime.utcnow)
    link_acesso = Column(String, nullable=True)  # Link da chamada de vídeo

    # Relacionamentos
    paciente = relationship("Paciente", back_populates="telemedicinas")
    profissional = relationship("ProfissionalSaude", back_populates="telemedicinas")