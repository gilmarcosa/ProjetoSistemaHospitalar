import pytest
from sqlalchemy.orm import Session
from app.models.profissionalSaude import ProfissionalSaude
from app.models.internacao import Internacao
from app.models.profissionalInternacao import ProfissionalInternacao
from datetime import datetime, date

def test_profissional_internacao(db: Session):
    # Criando um profissional de saúde
    profissional = ProfissionalSaude(nome="Dr. João", especialidade="Cardiologia")
    db.add(profissional)
    db.commit()
    db.refresh(profissional)

    # Criando uma internação
    internacao = Internacao(paciente_id=1,
                            leito_id=1,
                            data_entrada=date(2024, 3, 30), status="Ativo")

    db.add(internacao)
    db.commit()
    db.refresh(internacao)

    # Criando a relação na tabela intermediária ProfissionalInternacao
    relacao = ProfissionalInternacao(profissional_id=profissional.id, internacao_id=internacao.id)
    db.add(relacao)
    db.commit()
    db.refresh(relacao)

    # Verificando se a relação foi criada corretamente
    assert relacao.profissional_id == profissional.id
    assert relacao.internacao_id == internacao.id

    # Verificando a conexão bidirecional (se a internação está associada ao profissional)
    profissional_internacoes = db.query(ProfissionalInternacao).filter_by(profissional_id=profissional.id).all()
    assert len(profissional_internacoes) == 1
    assert profissional_internacoes[0].internacao_id == internacao.id
