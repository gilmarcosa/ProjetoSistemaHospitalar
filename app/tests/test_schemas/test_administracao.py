from app.schemas.administracao import AdministracaoRead

def test_administracao_read():
    admin = AdministracaoRead(id=1, nome="João", cargo="Coordenador Geral")
    assert admin.nome == "João"
    assert admin.cargo == "Coordenador Geral"
