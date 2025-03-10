from fastapi import APIRouter

from .auth import router as auth_router
from .license_routes import router as license_router
from .renewal_requests import router as requests_router
from .users import router as users_router

router = APIRouter()
router.include_router(auth_router)
router.include_router(license_router)
router.include_router(requests_router)
router.include_router(users_router)

__all__ = ['router']
