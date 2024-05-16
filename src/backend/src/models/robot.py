import ormar
from database.postgres import base_ormar_config
from ormar import Boolean, Integer, Model, String, ForeignKey, Optional
from models.user import User

class Robot(Model):
	ormar_config = base_ormar_config.copy(tablename="robots")

	id = Integer(primary_key=True, autoincrement=True)
	name = String(max_length=100)
	user_id: Optional[User] = ForeignKey(User)