import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.database import Base
from app.models.profissionalSaude  import ProfissionalSaude

class TestProfissionalSaude(unittest.TestCase):

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

    def test_criar_profissional_saude(self):
        """Testa a criação de um profissional de saúde."""
        profissional = ProfissionalSaude(
            nome="Dr. João",
            especialidade="Cardiologia"
        )
        self.session.add(profissional)
        self.session.commit()

        profissional_db = self.session.query(ProfissionalSaude).filter_by(nome="Dr. João").first()
        self.assertEqual(profissional_db.nome, "Dr. João")
        self.assertEqual(profissional_db.especialidade, "Cardiologia")

    def test_buscar_profissional_saude(self):
        """Testa a busca de um profissional de saúde."""
        profissional = ProfissionalSaude(
            nome="Dra. Maria",
            especialidade="Dermatologia"
        )
        self.session.add(profissional)
        self.session.commit()

        profissional_db = self.session.query(ProfissionalSaude).filter_by(nome="Dra. Maria").first()
        self.assertEqual(profissional_db.especialidade, "Dermatologia")

if __name__ == '__main__':
    unittest.main()