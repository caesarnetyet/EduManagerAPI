from pydantic import BaseModel
import datetime

class Subject(BaseModel):
    id: str
    name: str
    description: str
    units: list
    created_at: datetime.datetime
    updated_at: datetime.datetime
    deleted_at: datetime.datetime