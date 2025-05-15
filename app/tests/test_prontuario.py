import pytest
from sqlalchemy.orm import Session
from datetime import date
from app.models import Paciente, ProfissionalSaude
from app.models import prontuario
from app.models.prontuario import Prontuario


def test_criar_prontuario(db: Session):
    # Criando um paciente
    paciente = Paciente(
        nome="Carlos Andrade",
        data_nascimento=date(1990, 5, 20),
        historico_clinico="Nenhum problema registrado"
    )
    db.add(paciente)
    db.commit()
    db.refresh(paciente)

    # Criando um profissional de saúde
    profissional = ProfissionalSaude(
        nome="Dra. Fernanda Lopes",
        especialidade="Cardiologia"
    )
    db.add(profissional)
    db.commit()
    db.refresh(profissional)

    # Criando um prontuário
    prontuario = Prontuario(
        paciente_id=paciente.id,
        profissional_id=profissional.id,
        receita= "carai de asa",
        diagnostico="Hipertensão leve",
        observacoes="Recomendada atividade física e dieta balanceada"
    )
    db.add(prontuario)
    db.commit()
    db.refresh(prontuario)

    # Validações
    assert prontuario.id is not None
    assert prontuario.paciente_id == paciente.id
    assert prontuario.profissional_id == profissional.id
    assert prontuario.diagnostico == "Hipertensão leve"
    assert prontuario.observacoes == "Recomendada atividade física e dieta balanceada"

    # Verificando relações
    assert prontuario.paciente == paciente
    assert prontuario.profissional == profissional
