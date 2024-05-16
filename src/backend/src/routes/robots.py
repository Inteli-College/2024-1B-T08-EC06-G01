from fastapi import APIRouter
import ormar
import ormar.exceptions

from schemas.robots import Robot
from models.robots import Robot as RobotModel

router = APIRouter(
	prefix="/robots",
	tags=["robots"],
)

@router.post("/register")
async def register(user: Robot):
	return await RobotModel.objects.create(
		name=user.name,
		user_id=user.user_id
	)


