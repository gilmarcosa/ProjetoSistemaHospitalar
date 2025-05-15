from app.schemas.profissionalInternacao import ProfissionalInternacaoRead

def test_profissional_internacao():
    pi = ProfissionalInternacaoRead(
        id=1,
        profissional_id=2,
        internacao_id=3
    )
    assert pi.profissional_id == 2
