from fastapi import APIRouter

from src.persistence.data_manager import DataManager
from src.models.task import EventTask


router = APIRouter()

print("Starting HTTP RESTful API Server ...")

dataManager = DataManager()


@router.post("/tasks/")
async def new_event_task(newTask: EventTask):
    dataManager.add_task(newTask)
    return {"project_reference": newTask.project_reference}


@router.get("/tasks/")
async def get_all_tasks():
    return {"all_tasks": dataManager.get_all_tasks()}


@router.get("/tasks/{project_reference}")
async def get_project_tasks(project_reference: str):
    return {"project_tasks": dataManager.get_project_tasks(project_reference)}


@router.get("/tasks/projects/{assigned_to}")
async def get_assignee_tasks(assigned_to: str):
    return {"assignee_tasks": dataManager.get_assignee_tasks(assigned_to)}


@router.delete("/tasks/{project_reference}")
async def discard_project_tasks(project_reference: str):
    dataManager.delete_project_tasks(project_reference)
    return {"discard": "ok"}


@router.delete("/tasks/projects/{assigned_to}")
async def discard_assignee_tasks(assigned_to: str):
    dataManager.delete_assignee_tasks(assigned_to)
    return {"discard": "ok"}
