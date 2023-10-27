from typing import Annotated

from fastapi import APIRouter, Depends

from src.persistence.data_manager import dataManager
from src.models.requests import StaffRequest
from src.utils.auth import auth_production_manager, auth_hr_manager


router = APIRouter()

print("Starting HTTP RESTful API Server ...")


@router.post("/staff_requests/")
async def new_staff_request(
    newRequest: StaffRequest,
    authorized: Annotated[bool, Depends(auth_production_manager)],
):
    dataManager.add_staff_request(newRequest)
    return {"add": "ok"}


@router.get("/staff_requests/")
async def get_staff_requests(authorized: Annotated[bool, Depends(auth_hr_manager)]):
    return {"staff_requests": dataManager.get_staff_requests()}


@router.put("/staff_requests/")
async def discard_event_request(
    oldRequest: StaffRequest, authorized: Annotated[bool, Depends(auth_hr_manager)]
):
    dataManager.delete_staff_request(oldRequest)
    return {"delete": "ok"}
