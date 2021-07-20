from app.api.api_v1.endpoints import competitions
from app.api.api_v1.endpoints import login
from app.api.api_v1.endpoints import teams
from app.api.api_v1.endpoints import users
from app.api.api_v1.endpoints import rescue
from app.api.api_v1.endpoints import onstage
from app.api.api_v1.endpoints import soccer
from app.api.api_v1.endpoints import awards

from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, tags=["login"])
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(teams.router, prefix="/teams", tags=["teams"])
api_router.include_router(
    competitions.router, prefix="/competitions", tags=["competitions"]
)
api_router.include_router(rescue.router, prefix="/rescue", tags=["rescue"])
api_router.include_router(onstage.router, prefix="/onstage", tags=["onstage"])
api_router.include_router(soccer.router, prefix="/soccer", tags=["soccer"])
api_router.include_router(awards.router, prefix="/awards", tags=["awards"])
