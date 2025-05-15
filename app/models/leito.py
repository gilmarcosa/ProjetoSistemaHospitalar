from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from app.database import Base

class Leito(Base):
    __tablename__ = "leito"

    id = Column(Integer, primary_key=True, index=True)
    numero = Column(Integer, unique=True, nullable=False)
    tipo = Column(String, nullable=False)
    status = Column(Boolean, default=True)  # True = disponível, False = ocupado

    internacoes = relationship("Internacao", back_populates="leito")
