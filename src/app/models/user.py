import ormar
from typing import Optional
from db import BaseMeta

class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "user"

    id: int = ormar.Integer(primary_key=True, autoincrement=True, foreign_key=True),
    username: str = ormar.String(max_length=255),
    password: str = ormar.String(max_length=255),
    type_user: bool = ormar.Boolean(nullable=False),