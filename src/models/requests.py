from pydantic import BaseModel
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
