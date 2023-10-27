import json
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


with open(
    "./src/data/financial_requests/financial_request_1.json", "r", encoding="utf-8"
) as f_in:
    financial_request_1 = json.load(f_in)


def test_add_request1():
    response = client.post(
        "/financial_requests/", json=financial_request_1, auth=("natalie", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {
        "project_reference": financial_request_1["project_reference"]
    }


def test_get_requests():
    response = client.get("/financial_requests/", auth=("alice", "pswd"))
    assert response.status_code == 200
    assert response.json() == {
        "financial_requests": {
            financial_request_1["project_reference"]: financial_request_1
        }
    }


def test_get_request():
    response = client.get(
        f'/financial_requests/{financial_request_1["project_reference"]}',
        auth=("alice", "pswd"),
    )
    assert response.status_code == 200
    assert response.json() == {"financial_request": financial_request_1}


def test_discard_request():
    response = client.delete(
        f'/financial_requests/{financial_request_1["project_reference"]}',
        auth=("alice", "pswd"),
    )
    assert response.status_code == 200
    assert response.json() == {"discard": "ok"}
