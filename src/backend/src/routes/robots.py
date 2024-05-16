from fastapi import APIRouter
import ormar
import ormar.exceptions

from schemas.users import User
from models.users import User as UserModel
from utils.crypto import get_password_hash, verify_password

router = APIRouter(
	prefix="/users",
	tags=["users"],
)

@router.post("/register")
async def register(user: User):
	return await UserModel.objects.create(
		username=user.username,
		password=get_password_hash(user.password),
		admin=False
	)

@router.post("/login")
async def login(user: User):
	try:
		result = await UserModel.objects.get(username=user.username)

		if verify_password(user.password, result.password):
			return result
		else:
			return {"error": "Invalid password"}
	except ormar.exceptions.NoMatch:
		return {"error": "User not found"}

