from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Location(BaseModel):
	id: int = Field(default=None, gt=0)
	location_x: float = Field(default=None)
	location_y: float = Field(default=None)
	robot_id: int = Field(default=None)
	date: Optional[datetime] = Field(default=None)