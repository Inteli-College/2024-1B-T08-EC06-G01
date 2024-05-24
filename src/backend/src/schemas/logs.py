from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, Field


class Log(BaseModel):
    id: int = Field(default=None, gt=0)
    media_uuid: Optional[UUID] = Field(default=None)
    action: str = Field(default=None, max_length=100)
    date: Optional[datetime] = Field(default=None)
    type: bool = Field(default=False)