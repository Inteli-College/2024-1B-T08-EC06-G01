import ormar
from database.postgres import base_ormar_config
from ormar import Boolean, Integer, Model, String, ForeignKey, Optional, DateTime
from models.media import Media
from datetime import datetime  

class Log(Model):
    ormar_config = base_ormar_config.copy(tablename="logs")

    id = Integer(primary_key=True, autoincrement=True)
    media_uuid: Optional[Media] = ForeignKey(Media)
    action = String(max_length=100)
    date: DateTime = DateTime(default=datetime.now)
    type = Boolean()

