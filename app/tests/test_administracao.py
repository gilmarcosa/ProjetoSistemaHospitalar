import pytest
from sqlalchemy.orm import Session
from app.models.administracao import Administracao
from app.models.paciente import Paciente
from app.models.internacao import Internacao
from datetime import date

def test_criar_administracao(db: Session):
    # Criando um administrador
    admin = Administracao(nome="Carlos Silva", cargo="Coordenador")
    db.add(admin)
    db.commit()
    db.refresh(admin)

    assert admin.id is not None
    assert admin.nome == "Carlos Silva"
    assert admin.cargo == "Coordenador"

def test_administracao_gerencia_paciente(db: Session):
    # Criando um administrador
    admin = Administracao(nome="Ana Souza", cargo="Supervisora")
    db.add(admin)
    db.commit()
    db.refresh(admin)

    # Criando um paciente vinculado ao administrador
    paciente = Paciente(nome="João Pereira", data_nascimento=date(1990, 5, 15), administracao_id=admin.id)
    db.add(paciente)
    db.commit()
    db.refresh(paciente)

    assert paciente.administracao_id == admin.id
    assert paciente.administrador.nome == "Ana Souza"

def test_administracao_gerencia_internacao(db: Session):
    # Criando um administrador
    admin = Administracao(nome="Fernanda Lima", cargo="Gestora de Leitos")
    db.add(admin)
    db.commit()
    db.refresh(admin)

    # Criando uma internação associada ao administrador
    internacao = Internacao(paciente_id=1, leito_id=1, data_entrada=date.today(), administracao_id=admin.id)
    db.add(internacao)
    db.commit()
    db.refresh(internacao)

    assert internacao.administracao_id == admin.id
    assert internacao.administrador.nome == "Fernanda Lima"
