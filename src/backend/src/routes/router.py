from fastapi import APIRouter

from routes.users import router as users_router
# from routes.logs import router as logs_router
# from routes.medias import router as medias_router
from routes.robots import router as robots_router

router = APIRouter()

router.include_router(users_router)
# router.include_router(logs_router)
# router.include_router(medias_router)
router.include_router(robots_router)
