from app.schemas.consulta import ConsultaRead
from datetime import time

def test_consulta_read():
    consulta = ConsultaRead(
        id=1,
        paciente_id=1,
        profissional_id=2,
        status="Confirmada",
        hora=time(14, 30)
    )
    assert consulta.status == "Confirmada"
