from fastapi.testclient import TestClient
from task import app

client = TestClient(app)


def test_create_task():
    response = client.post("/tasks", json={"title": "Test task"})
    assert response.status_code == 200
    assert response.json()["task"]["title"] == "Test task"
