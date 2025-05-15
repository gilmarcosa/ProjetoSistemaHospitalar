from app.schemas.telemedicina import TelemedicinaRead
from datetime import datetime

def test_telemedicina_read():
    tele = TelemedicinaRead(
        id=1,
        paciente_id=1,
        profissional_id=2,
        status="Finalizada",
        horario=datetime.now(),
        link_acesso="https://reuniao.com/chamada"
    )
    assert tele.status == "Finalizada"
