from app.schemas.team_member import TeamMemberInDB
from typing import Any
from typing import List

from app import crud
from app import models
from app import schemas
from app.api import deps
from app.crud import base
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from pydantic.types import UUID4
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get("/", response_model=List[schemas.TeamApi])
async def read_teams(
    db: AsyncSession = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Retrieve users.
    """
    base_team = await crud.team.get_multi(db, skip=skip, limit=limit)
    team = []
    for _team in base_team:
        team.append(
            schemas.TeamApi(
                **_team.__dict__,
                team_members=crud.team.get_team_members(db, _team.uuid),
            )
        )
    return team


@router.post("/", response_model=schemas.Team)
async def create_team(
    *,
    db: AsyncSession = Depends(deps.get_db),
    team_in: schemas.TeamCreate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Create new team.
    """
    team = await crud.team.create(db, obj_in=team_in)
    return team


@router.get("/{team_uuid}", response_model=schemas.Team)
async def read_team_by_uuid(
    team_uuid: UUID4,
    current_user: models.User = Depends(deps.get_current_active_user),
    db: AsyncSession = Depends(deps.get_db),
) -> Any:
    """
    Get a specific team by uuid.
    """
    team = await crud.team.get(db, uuid=team_uuid)
    if not await crud.user.is_superuser(current_user):
        raise HTTPException(
            status_code=400, detail="The user doesn't have enough privileges"
        )
    return team


@router.put("/{team_uuid}", response_model=schemas.Team)
async def update_team(
    *,
    db: AsyncSession = Depends(deps.get_db),
    team_uuid: UUID4,
    team_in: schemas.TeamUpdate,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    """
    Update a team.
    """
    team = await crud.team.get(db, uuid=team_uuid)
    if not team:
        raise HTTPException(
            status_code=404,
            detail="The team with this uuid does not exist in the system",
        )
    team = await crud.team.update(db, db_obj=team, obj_in=team_in)
    return team


@router.get("/members/{team_uuid}", response_model=List[TeamMemberInDB])
async def get_team_members(
    *,
    db: AsyncSession = Depends(deps.get_db),
    team_uuid: UUID4,
    current_user: models.User = Depends(deps.get_current_active_superuser),
) -> Any:
    members = await crud.team.get_team_members(db, uuid=team_uuid)
    return members
