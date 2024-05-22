from fastapi import APIRouter, HTTPException
import ormar
from fastapi.responses import JSONResponse
from datetime import datetime
from uuid import UUID
import logging

from schemas.logs import Log
from models.logs import Log as LogModel

router = APIRouter(
    prefix="/logs",
    tags=["logs"],
)

@router.post("/register")
async def register(log: Log):
    try:
        await LogModel.objects.create(
            date=datetime.now(),
            media_uuid=log.media_uuid,
            action=log.action,
            type=log.type,
        )
        return JSONResponse(content={
            "error": False,
            "message": "Log criado com sucesso"
        }, status_code=201)
    except Exception as e:
        return JSONResponse(content={
            "error": True,
            "message": f"Erro interno do servidor: {e}"
        }, status_code=500)

@router.get("/list")
async def list_logs():
    try:
        logs = await LogModel.objects.all()
        if not logs:
            return JSONResponse(content={
                "error": True,
                "message": "Nenhum log encontrado"
            }, status_code=404)
        
        log_dicts = []
        for log in logs:
            log_dict = log.dict()
            for key, value in log_dict.items():
                if isinstance(value, dict):  
                    if 'uuid' in value and isinstance(value['uuid'], UUID):  
                        log_dict[key] = str(value['uuid'])  
                elif isinstance(value, datetime):
                    log_dict[key] = value.isoformat()
            log_dicts.append(log_dict)
        
        return JSONResponse(content={
            "error": False,
            "message": "Logs encontrados com sucesso",
            "data": log_dicts
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

        log_dict = log.dict()
        for key, value in log_dict.items():
            if isinstance(value, dict):  
                if 'uuid' in value and isinstance(value['uuid'], UUID):  
                    log_dict[key] = str(value['uuid'])  
            elif isinstance(value, datetime):
                log_dict[key] = value.isoformat()
 
        return JSONResponse(content={
            "error": False,
            "log": log_dict
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
            media_uuid=log.media_uuid,
            action=log.action,
            type=log.type,
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