from pydantic import BaseModel, Field

class Robot(BaseModel):
	id: int = Field(default=None, gt=0)
	username: str = Field(default=None, max_length=100)
	robot_id: int = Field(default=None)