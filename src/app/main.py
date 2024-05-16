from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from db import database, User, Course, Section
from routers import (
    userRouter,
    courseRouter,
    sectionRouter,
    # pictureRouter,
    adminRouter,
)

app = FastAPI()

app.include_router(userRouter)
app.include_router(courseRouter)
app.include_router(sectionRouter)
# app.include_router(pictureRouter)
app.include_router(adminRouter)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)