import json
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


with open(
    "./src/data/event_requests/event_request_1.json", "r", encoding="utf-8"
) as f_in:
    event_request_1 = json.load(f_in)

with open(
    "./src/data/event_requests/event_request_2.json", "r", encoding="utf-8"
) as f_in:
    event_request_2 = json.load(f_in)


def test_add_request1():
    response = client.post(
        "/event_requests/", json=event_request_1, auth=("sarah", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"record_number": event_request_1["record_number"]}


def test_add_request2():
    response = client.post(
        "/event_requests/", json=event_request_2, auth=("sarah", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"record_number": event_request_2["record_number"]}


def test_get_requests():
    response = client.get("/event_requests/", auth=("janet", "pswd"))
    assert response.status_code == 200
    assert response.json() == {
        "event_requests": {
            event_request_1["record_number"]: event_request_1,
            event_request_2["record_number"]: event_request_2,
        }
    }


def test_get_request():
    response = client.get(
        f'/event_requests/{event_request_1["record_number"]}', auth=("janet", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"event_request": event_request_1}


def test_discard_request():
    response = client.delete(
        f'/event_requests/{event_request_1["record_number"]}', auth=("janet", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"discard": "ok"}
