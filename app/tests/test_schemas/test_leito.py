from app.schemas.leito import LeitoRead

def test_leito_read():
    leito = LeitoRead(id=1, numero=101, tipo="Enfermaria", status=True)
    assert leito.numero == 101
    assert leito.tipo == "Enfermaria"
