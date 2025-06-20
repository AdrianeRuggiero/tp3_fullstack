import pytest
from api.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Calculateur" in response.data

def test_sum(client):
    response = client.post("/sum", json={"a": 3, "b": 4})
    assert response.status_code == 200
    assert response.get_json() == {"result": 7}

def test_sum_missing_fields(client):
    response = client.post("/sum", json={"a": 5})
    assert response.status_code == 400
    assert "error" in response.get_json()
