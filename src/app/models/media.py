import ormar
from typing import Optional
from db import BaseMeta
from models.robot import Robot

class Media(ormar.Model):
    class Meta(BaseMeta):
        tablename = "media"

        id: int = ormar.Integer(primary_key=True, autoincrement=True, foreign_key=True),
        title: str = ormar.String(max_length=255),
        url: str = ormar.String(max_length=255),
        type: str = ormar.String(max_length=255),
        date: str = ormar.String(max_length=255),
        robot_id: Optional[Robot] = ormar.ForeignKey(Robot),
