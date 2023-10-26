from fastapi import APIRouter

from src.persistence.data_manager import dataManager
from src.models.requests import EventRequest


router = APIRouter()

print("Starting HTTP RESTful API Server ...")


@router.post("/event_requests/")
async def new_event_request(newRequest: EventRequest):
    dataManager.add_event_request(newRequest)
    return {"record_number": newRequest.record_number}


@router.get("/event_requests/")
async def get_event_requests():
    return {"event_requests": dataManager.get_event_requests()}


@router.get("/event_requests/{record_number}")
async def get_event_request(record_number: str):
    return {"event_request": dataManager.get_event_request(record_number)}


@router.delete("/event_requests/{record_number}")
async def discard_event_request(record_number: str):
    dataManager.delete_event_request(record_number)
    return {"discard": "ok"}
