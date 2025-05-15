import pytest
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

def test_criar_paciente():
    response = client.post("/pacientes/", json={
        "nome": "Maria Teste",
        "data_nascimento": "1995-08-20",
        "historico_clinico": "Histórico de teste"
    })
    assert response.status_code == 201 or response.status_code == 200
    assert response.json()["nome"] == "Maria Teste"
    assert "id" in response.json()

def test_listar_pacientes():
    response = client.get("/pacientes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_buscar_paciente():
    # Primeiro cria um paciente
    response_create = client.post("/pacientes/", json={
        "nome": "Paciente Buscar",
        "data_nascimento": "2000-01-01",
        "historico_clinico": "Nenhum problema"
    })
    paciente_id = response_create.json()["id"]

    # Agora busca ele
    response = client.get(f"/pacientes/{paciente_id}")
    assert response.status_code == 200
    assert response.json()["id"] == paciente_id

def test_atualizar_paciente():
    # Cria um paciente
    response_create = client.post("/pacientes/", json={
        "nome": "Paciente Atualizar",
        "data_nascimento": "1990-12-12",
        "historico_clinico": "Teste inicial"
    })
    paciente_id = response_create.json()["id"]

    # Atualiza o paciente
    response_update = client.put(f"/pacientes/{paciente_id}", json={
        "nome": "Paciente Atualizado",
        "data_nascimento": "1990-12-12",
        "historico_clinico": "Teste atualizado"
    })
    assert response_update.status_code == 200
    assert response_update.json()["nome"] == "Paciente Atualizado"

def test_deletar_paciente():
    # Cria um paciente
    response_create = client.post("/pacientes/", json={
        "nome": "Paciente Deletar",
        "data_nascimento": "1988-05-10",
        "historico_clinico": "Apagar depois"
    })
    paciente_id = response_create.json()["id"]

    # Deleta o paciente
    response_delete = client.delete(f"/pacientes/{paciente_id}")
    assert response_delete.status_code == 200

    # Tenta buscar o paciente deletado
    response_get = client.get(f"/pacientes/{paciente_id}")
    assert response_get.status_code == 404

