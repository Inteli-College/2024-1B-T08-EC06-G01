import ormar
from typing import Optional
from db import BaseMeta
from models.user import User
from models.robot import Robot

class Logs(ormar.Model):
    class Meta(BaseMeta):
        tablename = "logs"

        id: int = ormar.Integer(primary_key=True, autoincrement=True, foreign_key=True),
        user_id: Optional[User] = ormar.ForeignKey(User),
        robot_id: Optional[Robot] = ormar.ForeignKey(Robot),
        date: str = ormar.String(max_length=255),
        time: str = ormar.String(max_length=255),
        action: str = ormar.String(max_length=255),
        type: str = ormar.String(max_length=255),