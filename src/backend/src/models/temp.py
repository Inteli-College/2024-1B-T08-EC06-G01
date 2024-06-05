from typing import Optional

from database.postgres import base_ormar_config
from models.robots import Robot
from ormar import ForeignKey, Integer, Model, Float

class Temp(Model):
    ormar_config = base_ormar_config.copy(tablename="temp")
    
    id = Integer(primary_key=True, autoincrement=True)
    temp = Float()
    robot_id: Optional[Robot] = ForeignKey(Robot)
