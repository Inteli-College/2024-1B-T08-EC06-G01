from pydantic import BaseModel, Field


class Temp(BaseModel):
	id: int = Field(default=None, gt=0)
	temp: float = Field(default=None)
	robot_id: int = Field(default=None)