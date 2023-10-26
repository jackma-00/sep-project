from fastapi import APIRouter

from src.persistence.data_manager import dataManager
from src.models.requests import FinancialRequest


router = APIRouter()

print("Starting HTTP RESTful API Server ...")


@router.post("/financial_requests/")
async def new_financial_request(newRequest: FinancialRequest):
    dataManager.add_financial_request(newRequest)
    return {"project_reference": newRequest.project_reference}


@router.get("/financial_requests/")
async def get_financial_requests():
    return {"financial_requests": dataManager.get_financial_requests()}


@router.get("/financial_requests/{project_reference}")
async def get_financial_request(project_reference: str):
    return {"financial_request": dataManager.get_financial_request(project_reference)}


@router.delete("/financial_requests/{project_reference}")
async def discard_financial_request(project_reference: str):
    dataManager.delete_financial_request(project_reference)
    return {"discard": "ok"}
