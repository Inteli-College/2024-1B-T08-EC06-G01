from fastapi import APIRouter
import ormar
import ormar.exceptions
from fastapi.responses import JSONResponse

from schemas.robots import Robot
from models.robots import Robot as RobotModel

router = APIRouter(
	prefix="/robots",
	tags=["robots"],
)

@router.post("/register")
async def register(robot: Robot):
	try:
		await RobotModel.objects.create(
			name=robot.name,
			user_id=robot.user_id
		)
		return JSONResponse(status_code=201, content={"message": "Robot created"})
	except ormar.exceptions.UniqueViolationError:
		return JSONResponse(status_code=400, content={"error": "Robot already exists"})

@router.get("/list")
async def list():
	return await RobotModel.objects.all()

@router.get("/get/{robot_id}")
async def get(robot_id: int):
	try:
		return await RobotModel.objects.get(id=robot_id)
	except ormar.exceptions.NoMatch:
		return None
	
@router.put("/update")
async def update(robot: Robot):
	await RobotModel.objects.update(
		robot.name,
		robot.user_id
	).where(RobotModel.id == robot.id)

@router.delete("/delete/{robot_id}")
async def delete(robot_id: int):
	await RobotModel.objects.delete(id=robot_id)
	return True




