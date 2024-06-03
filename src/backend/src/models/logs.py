from datetime import datetime
from typing import Optional

from database.postgres import base_ormar_config
from models.medias import Media
from models.users import User
from ormar import Boolean, DateTime, ForeignKey, Integer, Model, String


class Log(Model):
    ormar_config = base_ormar_config.copy(tablename="log")

    id = Integer(primary_key=True, autoincrement=True)
    date = DateTime(default=datetime.now)
    button_pressed = Boolean()  
    used_ia = Boolean()
    reliability = Optional[float]
    user_id: Optional[User] = ForeignKey(User)

