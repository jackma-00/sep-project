import json

from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials


security = HTTPBasic()


with open("./src/data/auth/roles.json", "r", encoding="utf-8") as f_in:
    roles = json.load(f_in)


def auth(username, role):
    if username in roles[role]:
        return True
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Unauthorized !",
        headers={"WWW-Authenticate": "Basic"},
    )


def auth_customer_service(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return auth(credentials.username, "customer_service")


def auth_customer_manager(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return auth(credentials.username, "customer_manager")


def auth_hr_manager(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return auth(credentials.username, "hr_manager")


def auth_financial_manager(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return auth(credentials.username, "financial_manager")


def auth_service_manager(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return auth(credentials.username, "service_manager")


def auth_production_manager(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return auth(credentials.username, "production_manager")


def auth_service_team(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return auth(credentials.username, "service_team")


def auth_production_team(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return auth(credentials.username, "production_team")
