from datetime import datetime
from app.models.paciente import Paciente
from app.models.profissionalSaude import ProfissionalSaude
from app.models.telemedicina import Telemedicina

def test_criar_consulta_telemedicina(db):
    # Criando um paciente fictício
    paciente = Paciente(nome="Carlos Silva", data_nascimento=datetime(1990, 5, 20), historico_clinico="Nenhum")
    db.add(paciente)
    db.commit()

    # Criando um profissional de saúde fictício
    profissional = ProfissionalSaude(nome="Dra. Fernanda Souza", especialidade="Cardiologia")
    db.add(profissional)
    db.commit()

    # Criando uma consulta de telemedicina
    consulta = Telemedicina(
        paciente_id=paciente.id,
        profissional_id=profissional.id,
        status="Agendado",
        horario=datetime(2025, 4, 1, 14, 30),
        link_acesso="https://videoconsulta.com/123"
    )

    db.add(consulta)
    db.commit()

    # Buscando a consulta no banco
    consulta_bd = db.query(Telemedicina).filter_by(id=consulta.id).first()

    # 🔥 Testando se os dados estão corretos
    assert consulta_bd is not None
    assert consulta_bd.paciente_id == paciente.id
    assert consulta_bd.profissional_id == profissional.id
    assert consulta_bd.status == "Agendado"
    assert consulta_bd.horario == datetime(2025, 4, 1, 14, 30)
    assert consulta_bd.link_acesso == "https://videoconsulta.com/123"

    # 🔗 Testando as relações
    assert consulta_bd.paciente.nome == "Carlos Silva"
    assert consulta_bd.profissional.nome == "Dra. Fernanda Souza"
