import ormar
import ormar.exceptions
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.location import Location as LocationModel
from schemas.location import Location

router = APIRouter(
	prefix="/location",
	tags=["location"],
)

@router.post("/register")
async def register(location: Location):
	try:
		await LocationModel.objects.create(
			location_x = location.location_x,
			location_y = location.location_y,
			robot_id = location.robot_id
		)
		return JSONResponse(content={
			"error": False,
			"message": "Location criado com sucesso"
		}, status_code=201)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.get("/list")
async def list():
	try:
		location = await LocationModel.objects.all()
		return JSONResponse(content={
			"error": False,
			"message": "Locations encontrados com sucesso",
			"data": location
		}, status_code=200)

	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.get("/get/{location_id}")
async def get(location_id: int):
	try:
		location = await LocationModel.objects.get(id=location_id)
		return JSONResponse(content={
			"error": False,
			"message": "Location encontrado com sucesso",
			"data": location
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Location não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.put("/update/{location_id}")
async def update(location_id: int, location: Location):
	try:
		await LocationModel.objects.update(location.dict(), id=location_id)
		return JSONResponse(content={
			"error": False,
			"message": "Location atualizado com sucesso"
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Location não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)
	

@router.delete("/delete/{location_id}")
async def delete(location_id: int):
	try:
		await LocationModel.objects.delete(id=location_id)
		return JSONResponse(content={
			"error": False,
			"message": "Location deletado com sucesso"
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Location não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)




