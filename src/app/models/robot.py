import ormar
from typing import Optional
from db import BaseMeta

class Robot(ormar.Model):
    class Meta(BaseMeta):
        tablename = "robot"

        id: int = ormar.Integer(primary_key=True, autoincrement=True, foreign_key=True),
        name: str = ormar.String(max_length=255),
