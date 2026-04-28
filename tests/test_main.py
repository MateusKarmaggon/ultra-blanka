from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root_status():
    response = client.get("/")
    assert response.status_code == 200

def test_root_content():
    response = client.get("/")
    assert response.json() == {"message": "sua resposta"}

def test_teste_status():
    response = client.get("/teste")
    assert response.status_code == 200

def test_teste_tem_numero():
    response = client.get("/teste")
    assert "numero" in response.json()

def test_teste_intervalo():
    response = client.get("/teste")
    numero = response.json()["numero"]
    assert 0 <= numero <= 100