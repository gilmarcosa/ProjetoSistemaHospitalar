# Sistema Hospitalar - Backend (FastAPI + SQLAlchemy)

# Como rodar o projeto

# 1. Clone o repositório:

No terminal:
git clone "https://github.com/gilmarcosa/ProjetoSistemaHospitalar"
cd "Projeto Sistema Hospitalar" (coloque o caminho da pasta onde se deseja clonar o repositorio)


no terminal navegue até o caminho onde você clonou o repositório, chegando lá crie e ative o ambiente virtual 

No terminal:
python -m venv venv
venv\\Scripts\\activate         # No Windows
source venv/bin/activate        # No Linux/macOS

Com o ambiente ativado rode o seguinte comando para que seja instalada as tecnologias necessarias

pip install -r requirements.txt


5 - navegue até a pasta raiz do projeto "/ProjetoSistemaHospitalar" e dê o comando para criar o servidor:

python -m app.createdb

6- rode esse codigo para ativar o servidor:

uvicorn app.main:app --reload

Acesse a documentação da API em: http://127.0.0.1:8000/docs
