from app.schemas.internacao import InternacaoRead
from datetime import date

def test_internacao_read():
    internacao = InternacaoRead(
        id=1,
        paciente_id=1,
        leito_id=2,
        data_entrada=date(2024, 3, 30),
        data_saida=None,
        status="Ativo",
        profissional_id=1,
        administracao_id=None
    )
    assert internacao.status == "Ativo"
