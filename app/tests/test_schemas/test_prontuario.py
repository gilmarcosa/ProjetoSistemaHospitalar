from app.schemas.prontuario import ProntuarioRead

def test_prontuario_read():
    prontuario = ProntuarioRead(
        id=1,
        paciente_id=1,
        profissional_id=2,
        diagnostico="Hipertensão",
        observacoes="Acompanhamento anual",
        receita="Losartana 50mg"
    )
    assert prontuario.diagnostico == "Hipertensão"
