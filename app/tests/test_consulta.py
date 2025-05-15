import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.consulta import Consulta
from datetime import time

class TestConsulta(unittest.TestCase):

    def setUp(self):
        """Configura o banco de dados de teste."""
        self.engine = create_engine('sqlite:///:memory:')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def tearDown(self):
        """Limpa o banco de dados de teste."""
        self.session.close()
        Base.metadata.drop_all(self.engine)

    def test_criar_consulta(self):
        """Testa a criação de uma consulta."""
        consulta = Consulta(
            profissional_id=1,  # Substitua pelo ID de um profissional existente
            status="Agendada",
            hora=time(10, 0)
        )
        self.session.add(consulta)
        self.session.commit()

        consulta_db = self.session.query(Consulta).filter_by(status="Agendada").first()
        self.assertEqual(consulta_db.status, "Agendada")
        self.assertEqual(consulta_db.hora, time(10, 0))

    def test_buscar_consulta(self):
        """Testa a busca de uma consulta."""
        consulta = Consulta(
            profissional_id=1,  # Substitua pelo ID de um profissional existente
            status="Cancelada",
            hora=time(14, 30)
        )
        self.session.add(consulta)
        self.session.commit()

        consulta_db = self.session.query(Consulta).filter_by(status="Cancelada").first()
        self.assertEqual(consulta_db.hora, time(14, 30))

if __name__ == '__main__':
    unittest.main()