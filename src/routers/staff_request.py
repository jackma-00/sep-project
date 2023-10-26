from fastapi import APIRouter

from src.persistence.data_manager import dataManager
from src.models.requests import StaffRequest


router = APIRouter()

print("Starting HTTP RESTful API Server ...")


@router.post("/staff_requests/")
async def new_staff_request(newRequest: StaffRequest):
    dataManager.add_staff_request(newRequest)
    return {"add": "ok"}


@router.get("/staff_requests/")
async def get_staff_requests():
    return {"staff_requests": dataManager.get_staff_requests()}


@router.put("/staff_requests/")
async def discard_event_request(oldRequest: StaffRequest):
    dataManager.delete_staff_request(oldRequest)
    return {"delete": "ok"}
