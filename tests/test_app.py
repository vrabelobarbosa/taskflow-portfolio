# tests/test_app.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from app import app, tarefas
import pytest

@pytest.fixture
def client():
    app.testing = True
    with app.test_client() as client:
        yield client

def test_listar_tarefas(client):
    tarefas.clear()
    tarefas.append({"titulo": "Teste listar", "status": "pendente", "prioridade": "Alta"})
    response = client.get("/tarefas")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["titulo"] == "Teste listar"

def test_criar_tarefa(client):
    tarefas.clear()
    nova = {"titulo": "Tarefa PyTest", "status": "pendente", "prioridade": "Média"}
    response = client.post("/tarefas", json=nova)
    assert response.status_code == 201
    data = response.get_json()
    assert data["titulo"] == "Tarefa PyTest"
    assert data["status"] == "pendente"

def test_editar_tarefa(client):
    tarefas.clear()
    tarefas.append({"titulo": "Editar", "status": "pendente", "prioridade": "Alta"})
    atualizacao = {"status": "concluída"}
    response = client.put("/tarefas/0", json=atualizacao)
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "concluída"

def test_deletar_tarefa(client):
    tarefas.clear()
    tarefas.append({"titulo": "Excluir", "status": "pendente", "prioridade": "Alta"})
    response = client.delete("/tarefas/0")
    assert response.status_code == 200
    data = response.get_json()
    assert data["titulo"] == "Excluir"