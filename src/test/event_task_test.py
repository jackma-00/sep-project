import json
from fastapi.testclient import TestClient

from src.main import app

client = TestClient(app)


with open("./src/data/tasks/task_1.json", "r", encoding="utf-8") as f_in:
    task_1 = json.load(f_in)

with open("./src/data/tasks/task_2.json", "r", encoding="utf-8") as f_in:
    task_2 = json.load(f_in)

with open("./src/data/tasks/task_3.json", "r", encoding="utf-8") as f_in:
    task_3 = json.load(f_in)


def test_add_task1():
    response = client.post("/tasks/", json=task_1, auth=("jack", "pswd"))
    assert response.status_code == 200
    assert response.json() == {"project_reference": task_1["project_reference"]}


def test_add_task2():
    response = client.post("/tasks/", json=task_2, auth=("jack", "pswd"))
    assert response.status_code == 200
    assert response.json() == {"project_reference": task_2["project_reference"]}


def test_add_task3():
    response = client.post("/tasks/", json=task_3, auth=("jack", "pswd"))
    assert response.status_code == 200
    assert response.json() == {"project_reference": task_3["project_reference"]}


def test_get_all_tasks():
    response = client.get("/tasks/", auth=("jack", "pswd"))
    assert response.status_code == 200
    assert response.json() == {
        "all_tasks": {
            task_1["project_reference"]: [task_1, task_2],
            task_3["project_reference"]: [task_3],
        }
    }


def test_assignee_tasks():
    response = client.get(
        f'/tasks/projects/{task_3["assign_to"]}', auth=("amber", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"assignee_tasks": [task_1, task_3]}


def test_discard_assignee_tasks():
    response = client.delete(
        f'/tasks/projects/{task_3["assign_to"]}', auth=("amber", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"discard": "ok"}


def test_discard_project_tasks():
    response = client.delete(
        f'/tasks/{task_3["project_reference"]}', auth=("jack", "pswd")
    )
    assert response.status_code == 200
    assert response.json() == {"discard": "ok"}


def test_get_all_tasks_repeat():
    response = client.get("/tasks/", auth=("jack", "pswd"))
    assert response.status_code == 200
    assert response.json() == {
        "all_tasks": {
            task_2["project_reference"]: [task_2],
        }
    }
