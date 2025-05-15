from app.schemas.profissionalSaude import ProfissionalSaudeRead

def test_profissional_saude_read():
    profissional = ProfissionalSaudeRead(id=1, nome="Dra. Ana", especialidade="Cardiologia")
    assert profissional.nome == "Dra. Ana"
    assert profissional.especialidade == "Cardiologia"