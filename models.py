from pydantic import BaseModel
from typing import Optional
from datetime import datetime

#db schema
class Incident(BaseModel):
    id: str
    title: str
    description: str
    severity: int
    status: str
    service: str
    root_cause: Optional[str] = None
    resolution: Optional[str] = None
    tags: list[str] = []
    created_at: datetime
    resolved_at: Optional[datetime] = None
