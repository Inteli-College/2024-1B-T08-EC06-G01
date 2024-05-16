from fastapi import APIRouter

from routes.users import router as users_router
from routes.logs import router as logs_router
from routes.media import router as media_router
from routes.robot import router as robot_router

router = APIRouter()

router.include_router(users_router)
router.include_router(logs_router)
router.include_router(media_router)
router.include_router(robot_router)
