from typing import Annotated

from fastapi import APIRouter, Depends

from src.persistence.data_manager import dataManager
from src.models.task import EventTask
from src.utils.auth import auth_production_manager, auth_production_team


router = APIRouter()

print("Starting HTTP RESTful API Server ...")


@router.post("/tasks/")
async def new_event_task(
    newTask: EventTask, authorized: Annotated[bool, Depends(auth_production_manager)]
):
    dataManager.add_task(newTask)
    return {"project_reference": newTask.project_reference}


@router.get("/tasks/")
async def get_all_tasks(authorized: Annotated[bool, Depends(auth_production_manager)]):
    return {"all_tasks": dataManager.get_all_tasks()}


@router.get("/tasks/{project_reference}")
async def get_project_tasks(
    project_reference: str,
    authorized: Annotated[bool, Depends(auth_production_manager)],
):
    return {"project_tasks": dataManager.get_project_tasks(project_reference)}


@router.get("/tasks/projects/{assigned_to}")
async def get_assignee_tasks(
    assigned_to: str, authorized: Annotated[bool, Depends(auth_production_team)]
):
    return {"assignee_tasks": dataManager.get_assignee_tasks(assigned_to)}


@router.delete("/tasks/{project_reference}")
async def discard_project_tasks(
    project_reference: str,
    authorized: Annotated[bool, Depends(auth_production_manager)],
):
    dataManager.delete_project_tasks(project_reference)
    return {"discard": "ok"}


@router.delete("/tasks/projects/{assigned_to}")
async def discard_assignee_tasks(
    assigned_to: str, authorized: Annotated[bool, Depends(auth_production_team)]
):
    dataManager.delete_assignee_tasks(assigned_to)
    return {"discard": "ok"}
