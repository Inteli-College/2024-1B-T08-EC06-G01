from datetime import datetime
from uuid import UUID

import ormar
from fastapi import APIRouter
from fastapi.responses import JSONResponse
from models.logs import Log as LogModel
from schemas.logs import Log

router = APIRouter(
    prefix="/logs",
    tags=["logs"],
)

# @router.post("/register")
# async def register(log: Log):
#     try:
#         await LogModel.objects.create(
#             date = log.date,
#             emergency_button = log.emergency_button,
#             ia_request = log.ia_request,
#             user_id = log.user_id
#         )
#         return JSONResponse(content={
#             "error": False,
#             "message": "Log criado com sucesso"
#         }, status_code=201)
#     except Exception as e:
#         return JSONResponse(content={
#             "error": True,
#             "message": f"Erro interno do servidor: {e}"
#         }, status_code=500)

@router.get("/list")
async def list_logs():
    try:
        logs = await LogModel.objects.all()
        if not logs:
            return JSONResponse(content={
                "error": True,
                "message": "Nenhum log encontrado"
            }, status_code=404)
        return JSONResponse(content={
            "error": False,
            "message": "Logs encontrados com sucesso",
            "data": logs
        }, status_code=200)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)

@router.get("/list/{log_id}")
async def list(log_id: int):
    try:
        log = await LogModel.objects.get(id=log_id)
        print(log)
        return JSONResponse(content={
            "error": False,
            "log": log
        }, status_code=200)
    except ormar.NoMatch:
        return JSONResponse(content={
            "error": True,
            "message": "Log não encontrado"
        }, status_code=404)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)

@router.put("/update")
async def update(log: Log):
    try:
        await LogModel.objects.filter(id=log.id).update(
            date = log.date,
            emergency_button = log.emergency_button,
            ia_request = log.ia_request,
            user_id = log.user_id,
            username = log.username
        )
        return JSONResponse(content={
            "error": False,
            "message": "Log atualizado com sucesso"
        }, status_code=200)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)

@router.delete("/delete/{log_id}")
async def delete(log_id: int):
    try:
        await LogModel.objects.delete(id=log_id)
        return JSONResponse(content={
            "error": False,
            "message": "Log deletado com sucesso"
        }, status_code=200)
    except ormar.NoMatch:
        return JSONResponse(content={
            "error": True,
            "message": "Log não encontrado"
        }, status_code=404)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)