from datetime import date
from sqlalchemy.orm import Session
from app.models import Paciente, ProfissionalSaude, prontuario  # Ajuste o caminho conforme necessário
from app.models.prontuario import Prontuario
from app.models.receita import Receita


def test_criar_receita(db: Session):
    # Criando um paciente
    paciente = Paciente(
        nome="João Silva",
        data_nascimento=date(1990, 5, 20),
        historico_clinico="Nenhum histórico relevante"
    )
    db.add(paciente)
    db.commit()
    db.refresh(paciente)

    # Criando um profissional de saúde
    profissional = ProfissionalSaude(
        nome="Dra. Maria",
        especialidade="Cardiologista"

    )
    db.add(profissional)
    db.commit()
    db.refresh(profissional)

    prontuario = Prontuario(
        paciente_id=paciente.id,
        profissional_id=profissional.id,  # ✅ Agora tem um profissional
        diagnostico="Hipertensão",
        observacoes="Acompanhamento anual"
    )
    db.add(prontuario)
    db.commit()

    # Criando uma receita associando paciente e profissional de saúde
    receita = Receita(
        paciente_id=paciente.id,
        profissional_id=profissional.id,
        prontuario_id=prontuario.id,
        medicamento="Losartana 50mg",
        observacoes="Tomar 1 comprimido ao dia",
        dosagem="50mg",
        validade=date(2025, 1, 1)
    )
    db.add(receita)
    db.commit()
    db.refresh(receita)

    # Verificando se os dados foram salvos corretamente
    assert receita.id is not None
    assert receita.paciente_id == paciente.id
    assert receita.profissional_id == profissional.id
    assert receita.prontuario_id == prontuario.id
    assert receita.medicamento == "Losartana 50mg"
    assert receita.observacoes == "Tomar 1 comprimido ao dia"
    assert receita.dosagem == "50mg"
    assert receita.validade == date(2025, 1, 1)
