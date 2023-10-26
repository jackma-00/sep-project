from pydantic import BaseModel


class EventTask(BaseModel):
    project_reference: str
    description: str
    assign_to: str
    priority: str
