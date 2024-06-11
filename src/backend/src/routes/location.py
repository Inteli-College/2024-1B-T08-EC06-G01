import ormar
import ormar.exceptions
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.location import Location as LocationModel
from schemas.location import Location
from pytz import timezone
from datetime import datetime

router = APIRouter(
	prefix="/location",
	tags=["location"],
)

@router.post("/register")
async def register(location: Location):
	try:
		current_time = datetime.now(tz=timezone('America/Sao_Paulo'))
		current_time_naive = current_time.replace(tzinfo=None)

		await LocationModel.objects.create(
			location_x=location.location_x,
			location_y=location.location_y,
			robot_id=location.robot_id,
			date=current_time_naive,
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
		if not location:
			return JSONResponse(content={
				"error": True,
				"message": "Nenhum location encontrado"
			}, status_code=404)
		location_dicts = []
		for location in location:
			location_dict = location.dict()
			for key, value in location_dict.items():
				if isinstance(value, float):
					location_dict[key] = float(value)
				if isinstance(value, datetime):
					location_dict[key] = value.isoformat()
			location_dicts.append(location_dict)
	
		return JSONResponse(content={
			"error": False,
			"message": "Locations encontrados com sucesso",
			"data": location_dicts
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

		if not location:
			return JSONResponse(content={
				"error": True,
				"message": "Location não encontrado"
			}, status_code=404)
		
		location_dict = location.dict()
		for key, value in location_dict.items():
			if isinstance(value, float):
				location_dict[key] = float(value)
			if isinstance(value, datetime):
				location_dict[key] = value.isoformat()

		return JSONResponse(content={
			"error": False,
			"message": "Location encontrado com sucesso",
			"data": location_dict
		}, status_code=200)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.put("/update/{location_id}")
async def update(location_id: int, location_update: Location):
    try:
        existing_location = await LocationModel.objects.get(id=location_id)
        
        updated_fields = location_update.dict(exclude_unset=True)

        if 'date' in updated_fields:
            del updated_fields['date']

        for key, value in updated_fields.items():
            setattr(existing_location, key, value)

        await existing_location.update()

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




