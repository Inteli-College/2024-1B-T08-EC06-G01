import ormar
import ormar.exceptions
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.temp import Temp as TempModel
from schemas.temp import Temp

router = APIRouter(
	prefix="/temp",
	tags=["temp"],
)

@router.post("/register")
async def register(temp: Temp):
	try:
		await TempModel.objects.create(
			temp=temp.temp,
            robot_id=temp.robot_id
		)
		return JSONResponse(content={
			"error": False,
			"message": "Temp criado com sucesso"
		}, status_code=201)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.get("/list")
async def list():
	try:
		temp = await TempModel.objects.all()
		return JSONResponse(content={
			"error": False,
			"message": "Temp encontrados com sucesso",
			"data": temp
		}, status_code=200)

	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.get("/get/{temp_id}")
async def get(temp_id : int):
	try:
		temp = await TempModel.objects.get(id=temp_id)
		return JSONResponse(content={
			"error": False,
			"message": "Temp encontrado com sucesso",
			"data": temp
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Temp não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.put("/update/{temp_id}")
async def update(temp_id: int, temp: Temp):
    try:
        await TempModel.objects.update(temp.dict(), id=temp_id)
        return JSONResponse(content={
            "error": False,
            "message": "Temp atualizado com sucesso"
        }, status_code=200)
    except ormar.exceptions.NoMatch:
        return JSONResponse(content={
            "error": True,
            "message": "Temp não encontrado"
        }, status_code=404)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)


@router.delete("/delete/{temp_id}")
async def delete(temp_id: int):
	try:
		await TempModel.objects.delete(id=temp_id)
		return JSONResponse(content={
			"error": False,
			"message": "Temp deletado com sucesso"
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Temp não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)




