import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.database import get_db

# Criando um banco de dados SQLite em memória para testes
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db():
    """Cria uma sessão do banco de dados para testes."""
    Base.metadata.create_all(bind=engine)  # Cria as tabelas no banco de dados de teste
    session = TestingSessionLocal()
    yield session  # Fornece a sessão para os testes
    session.close()  # Fecha a sessão após os testes
    Base.metadata.drop_all(bind=engine)  # Limpa o banco após os testes
