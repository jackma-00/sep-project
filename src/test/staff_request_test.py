import json
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


with open(
    "./src/data/staff_requests/staff_request_1.json", "r", encoding="utf-8"
) as f_in:
    staff_request_1 = json.load(f_in)


def test_add_request1():
    response = client.post(
        "/staff_requests/", json=staff_request_1, auth=("jack", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"add": "ok"}


def test_get_requests():
    response = client.get("/staff_requests/", auth=("simon", "pswd"))
    assert response.status_code == 200
    assert response.json() == {"staff_requests": [staff_request_1]}


def test_discard_request():
    response = client.put(
        "/staff_requests/", json=staff_request_1, auth=("simon", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"delete": "ok"}
