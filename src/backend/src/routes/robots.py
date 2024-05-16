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
async def register(robot: Robot):
	return await RobotModel.objects.create(
		name=robot.name,
		user_id=robot.user_id
	)


