from typing import Annotated

from fastapi import APIRouter, Depends

from src.persistence.data_manager import dataManager
from src.models.requests import FinancialRequest
from src.utils.auth import auth_production_manager, auth_financial_manager


router = APIRouter()

print("Starting HTTP RESTful API Server ...")


@router.post("/financial_requests/")
async def new_financial_request(
    newRequest: FinancialRequest,
    authorized: Annotated[bool, Depends(auth_production_manager)],
):
    dataManager.add_financial_request(newRequest)
    return {"project_reference": newRequest.project_reference}


@router.get("/financial_requests/")
async def get_financial_requests(
    authorized: Annotated[bool, Depends(auth_financial_manager)]
):
    return {"financial_requests": dataManager.get_financial_requests()}


@router.get("/financial_requests/{project_reference}")
async def get_financial_request(
    project_reference: str, authorized: Annotated[bool, Depends(auth_financial_manager)]
):
    return {"financial_request": dataManager.get_financial_request(project_reference)}


@router.delete("/financial_requests/{project_reference}")
async def discard_financial_request(
    project_reference: str, authorized: Annotated[bool, Depends(auth_financial_manager)]
):
    dataManager.delete_financial_request(project_reference)
    return {"discard": "ok"}
