import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.paciente import Paciente
from app.models.consulta import Consulta
from app.models.profissionalSaude import ProfissionalSaude  # Adicione esta linha
from datetime import date, time

class TestConsultaPaciente(unittest.TestCase):

    def setUp(self):
        """Configura o banco de dados de teste."""
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Cria um paciente para os testes
        paciente = Paciente(nome="Teste", data_nascimento=date(2000, 1, 1))
        self.session.add(paciente)
        self.session.commit()
        self.paciente_id = paciente.id

        # Cria um profissional de saúde para os testes
        profissional = ProfissionalSaude(nome="Dr. João", especialidade="Cardiologista")
        self.session.add(profissional)
        self.session.commit()
        self.profissional_id = profissional.id

    def tearDown(self):
        """Limpa o banco de dados de teste."""
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_criar_consulta_com_paciente(self):
        """Testa a criação de uma consulta com paciente."""
        consulta = Consulta(
            paciente_id=self.paciente_id,
            profissional_id=self.profissional_id,
            status="Agendada",
            hora=time(10, 0)
        )
        self.session.add(consulta)
        self.session.commit()

        consulta_db = self.session.query(Consulta).filter_by(paciente_id=self.paciente_id).first()
        self.assertEqual(consulta_db.paciente_id, self.paciente_id)

        paciente_db = self.session.query(Paciente).filter_by(id=self.paciente_id).first()
        self.assertEqual(len(paciente_db.consultas), 1)
        self.assertEqual(paciente_db.consultas[0].id, consulta_db.id)

    def test_buscar_consultas_do_paciente(self):
        """Testa a busca de consultas de um paciente."""
        consulta1 = Consulta(
            paciente_id=self.paciente_id,
            profissional_id=self.profissional_id,
            status="Agendada",
            hora=time(10, 0)
        )
        consulta2 = Consulta(
            paciente_id=self.paciente_id,
            profissional_id=self.profissional_id,
            status="Cancelada",
            hora=time(14, 30)
        )
        self.session.add_all([consulta1, consulta2])
        self.session.commit()

        paciente_db = self.session.query(Paciente).filter_by(id=self.paciente_id).first()
        self.assertEqual(len(paciente_db.consultas), 2)
        self.assertEqual(paciente_db.consultas[0].status, "Agendada")
        self.assertEqual(paciente_db.consultas[1].status, "Cancelada")

if __name__ == '__main__':
    unittest.main()