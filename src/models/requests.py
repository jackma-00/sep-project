from pydantic import BaseModel, conint
from datetime import date


class Preferences(BaseModel):
    decorations: bool
    parties: bool
    photos: bool
    food: bool
    drinks: bool


class EventRequest(BaseModel):
    record_number: str
    client_name: str
    event_type: str
    from_date: date
    to_date: date
    expected_attenders: int
    preferences: Preferences
    expected_budget: int


class StaffRequest(BaseModel):
    contract_type: conint(ge=0, le=1)
    requesting_department: conint(ge=0, le=3)
    years_of_experience: int
    job_title: str
    job_description: str


class FinancialRequest(BaseModel):
    requesting_department: conint(ge=0, le=3)
    project_reference: str
    required_amount: int
    reason: str
