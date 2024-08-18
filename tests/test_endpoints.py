import os
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.() == {"Hello": "World"}

def test_read_example():
    os.environ["API_KEY"] = "testkey"
    headers = {"X-API-KEY": "testkey"}
    response = client.get("/example", headers=headers)
    assert response.status_code == 200
    assert response.() == {"Example": "This is an example endpoint"}

def test_get_prediction():
    os.environ["API_KEY"] = "testkey"
    headers = {"X-API-KEY": "testkey"}
    data = {
        "model_id": "test_model",
        "input_data": {"key": "value"}
    }
    response = client.post("/predict", =data, headers=headers)
    assert response.status_code == 200
    assert "prediction" in response.()
