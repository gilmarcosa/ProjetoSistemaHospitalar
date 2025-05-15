from app.schemas.paciente import PacienteCreate, PacienteRead
from datetime import date

def test_paciente_create():
    paciente = PacienteCreate(
        nome="João da Silva",
        data_nascimento=date(1980, 5, 20),
        historico_clinico="Sem comorbidades"
    )

    assert paciente.nome == "João da Silva"
    assert paciente.data_nascimento == date(1980, 5, 20)
    assert paciente.historico_clinico == "Sem comorbidades"

def test_paciente_read():
    paciente = PacienteRead(
        id=1,
        nome="Maria Oliveira",
        data_nascimento=date(1992, 8, 15),
        historico_clinico="Alergia a penicilina"
    )

    assert paciente.id == 1
    assert paciente.nome == "Maria Oliveira"
    assert paciente.data_nascimento == date(1992, 8, 15)
    assert paciente.historico_clinico == "Alergia a penicilina"
