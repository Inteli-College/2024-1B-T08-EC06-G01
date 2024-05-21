import ormar
from database.postgres import base_ormar_config
from ormar import Boolean, Integer, Model, String, ForeignKey, UUID, DateTime
import uuid
from datetime import datetime  
from models.robots import Robot
from typing import Optional	

class Media(Model):
	ormar_config = base_ormar_config.copy(tablename="media")

	uuid: UUID = UUID(primary_key=True, default=uuid.uuid4)
	title = String(max_length=100)
	type = Boolean()
	date: DateTime = DateTime(default=datetime.now)
	robot_id: Optional[Robot] = ForeignKey(Robot)