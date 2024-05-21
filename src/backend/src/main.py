import os
import uvicorn
from fastapi import FastAPI

from dotenv import load_dotenv

# from middleware.crypto import guard

from database.postgres import database
from routes.router import router

load_dotenv('./.env')

assert os.environ.get('DATABASE_URL') != ""
assert os.environ.get('BUCKET_HOST') != ""
assert os.environ.get('BUCKET_PORT') != ""
assert os.environ.get('BUCKET_ACCESS_KEY') != ""
assert os.environ.get('BUCKET_SECRET_KEY') != ""
assert os.environ.get('BUCKET_USE_SSL') != ""
assert os.environ.get('JWT_SECRET') != ""
assert os.environ.get('AES_SECRET') != ""


app = FastAPI()

app.state.database = database

@app.on_event("startup")
async def startup() -> None:
    database_ = app.state.database
    if not database_.is_connected:
        await database_.connect()
        print("Database connected")

@app.on_event("shutdown")
async def shutdown() -> None:
    database_ = app.state.database
    if database_.is_connected:
        await database_.disconnect()

app.include_router(router)


if __name__ == "__main__":
	uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)