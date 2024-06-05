import ormar
import ormar.exceptions
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.users import User as UserModel
from schemas.users import User
from utils.crypto import get_password_hash, verify_password
from models.logs import Log as LogModel
from schemas.logs import Log

router = APIRouter(
	prefix="/users",
	tags=["users"],
)

@router.post("/register")
async def register(user: User):
	try:
		await UserModel.objects.create(
			username=user.username,
			password=get_password_hash(user.password),
			admin=False
		)
		return JSONResponse(content={
			"error": False,
			"message": "Usuário criado com sucesso"
		}, status_code=201)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.post("/login")
async def login(user: User):
	try:
		result = await UserModel.objects.get(username=user.username)

		if verify_password(user.password, result.password):
			create_log(user.id, user.username)
			return result
		else:
			return {"error": "Invalid password"}
	except ormar.exceptions.NoMatch:
		return {"error": "User not found"}
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)
	
async def create_log(user_id, username):
	try:
		await LogModel.objects.create(
			emergency_button=False,
			ia_request=False,
			user_id=user_id,
			username=username
		)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)


@router.get("/list")
async def list():
    try:
        users_all = await UserModel.objects.all()
        users_list = [user.dict() for user in users_all]
        return JSONResponse(content={
            "error": False,
            "message": "Usuários encontrados com sucesso",
            "data": users_list
        }, status_code=200)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)

@router.get("/get/{user_id}")
async def get(user_id: int):
	try:
		user = await UserModel.objects.get(id=user_id)
		user_dict = user.dict()
		return JSONResponse(content={
			"error": False,
			"message": "Usuário encontrado com sucesso",
			"data": user_dict
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Usuário não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.put("/update")
async def update(user: User):
	try:
		await UserModel.objects.filter(id=user.id).update(
			username=user.username,
			password=get_password_hash(user.password),
			admin=user.admin
		)
		return JSONResponse(content={
			"error": False,
			"message": "Usuário atualizado com sucesso"
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Usuário não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

@router.delete("/delete/{user_id}")
async def delete(user_id: int):
	try:
		await UserModel.objects.delete(id=user_id)
		return JSONResponse(content={
			"error": False,
			"message": "Usuário deletado com sucesso"
		}, status_code=200)
	except ormar.exceptions.NoMatch:
		return JSONResponse(content={
			"error": True,
			"message": "Usuário não encontrado"
		}, status_code=404)
	except Exception as e:
		return JSONResponse(content={
			"error": True,
			"message": f"Erro interno do servidor: {e}"
		}, status_code=500)

