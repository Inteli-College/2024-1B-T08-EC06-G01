from typing import Optional

from database.postgres import base_ormar_config
from ormar import ForeignKey, Integer, Model, Float
from models.robots import Robot

class Location(Model):
    ormar_config = base_ormar_config.copy(tablename="location")

    id = Integer(primary_key=True, autoincrement=True)
    location_x = Float()
    location_y = Float()
    robot_id: Optional[Robot] = ForeignKey(Robot)
