from app.schemas.receita import ReceitaRead
from datetime import date

def test_receita_read():
    receita = ReceitaRead(
        id=1,
        paciente_id=1,
        profissional_id=1,
        prontuario_id=1,
        medicamento="Paracetamol",
        observacoes="Tomar após refeições",
        dosagem="500mg",
        validade=date(2025, 1, 1)
    )
    assert receita.medicamento == "Paracetamol"
