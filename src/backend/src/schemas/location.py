from pydantic import BaseModel, Field


class Location(BaseModel):
	id: int = Field(default=None, gt=0)
	location_x: float = Field(default=None)
	location_y: float = Field(default=None)
	robot_id: int = Field(default=None)