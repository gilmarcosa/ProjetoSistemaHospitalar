from datetime import date, datetime
from sqlalchemy.orm import Session
from app.models.paciente import Paciente
from app.models.leito import Leito
from app.models.internacao import Internacao

def test_criar_internacao(db: Session):
    # Criar um paciente
    paciente = Paciente(nome="João Silva", data_nascimento= date(1985, 6, 15), historico_clinico="Hipertensão")
    db.add(paciente)
    db.commit()
    db.refresh(paciente)

    # Criar um leito
    leito = Leito(numero=101, tipo="Enfermaria", status=True)
    db.add(leito)
    db.commit()
    db.refresh(leito)

    # Criar uma internação
    internacao = Internacao(
        paciente_id=paciente.id,
        leito_id=leito.id,
        data_entrada=date(1985, 6, 15),
        status="Ativo"
    )
    db.add(internacao)
    db.commit()
    db.refresh(internacao)

    # Verificar se a internação foi criada corretamente
    assert internacao.paciente_id == paciente.id
    assert internacao.leito_id == leito.id
    assert internacao.status == "Ativo"

    # Verificar os relacionamentos
    assert internacao.paciente == paciente
    assert internacao.leito == leito

    print("✅ Teste de internação passou!")

