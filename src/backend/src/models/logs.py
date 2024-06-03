from datetime import datetime
from typing import Optional

from database.postgres import base_ormar_config
from models.medias import Media
from ormar import Boolean, DateTime, ForeignKey, Integer, Model, String


class Log(Model):
    ormar_config = base_ormar_config.copy(tablename="log")

    id = Integer(primary_key=True, autoincrement=True)
    media_uuid: Optional[Media] = ForeignKey(Media)
    date = DateTime(default=datetime.now)
    used_ia = Boolean()
    reliability = Optional[float]

