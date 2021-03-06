from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from app.crud.base import CRUDBase
from app.models.team import Team
from app.models.team import TeamMember
from app.schemas.team import TeamCreate
from app.schemas.team import TeamUpdate
from pydantic.types import UUID4


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    async def create(self, db: AsyncSession, *, obj_in: TeamCreate) -> Team:
        db_obj = Team(
            uuid=uuid4(),
            name=obj_in.name,
            organisation=obj_in.organisation,
            num_member=len(obj_in.team_members),
            uuid_mentor=obj_in.uuid_mentor,
            hardware_type=obj_in.hardware_type,
            software_type=obj_in.software_type,
            uuid_competition=obj_in.uuid_competition,
        )
        await db.add(db_obj)
        await db.commit()
        for member in obj_in.team_members:
            mem_obj = TeamMember(
                uuid=uuid4(),
                uuid_user=member.uuid,
                uuid_team=db_obj.uuid,
                role=member.role,
            )
            await db.add(mem_obj)
        await db.commit()
        db.refresh(db_obj)
        return db_obj

    async def get_team_members(self, db: AsyncSession, uuid: UUID4) -> List[TeamMember]:
        result = await db.execute(select(TeamMember).filter(TeamMember.uuid_team == uuid))
        return result.scalars().all()

    async def update(
        self, db: AsyncSession, *, db_obj: Team, obj_in: Union[TeamUpdate, Dict[str, Any]]
    ) -> Team:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return await super().update(db, db_obj=db_obj, obj_in=update_data)

    async def get_by_user(self, db: AsyncSession, uuid: UUID4) -> List[Team]:
        team_members: List[TeamMember] = await db.execute(select(TeamMember).filter(TeamMember.uuid_team == uuid))
        teams = []
        for team in team_members:
            teams.append(await db.execute(select(Team).filter(Team.uuid == team.uuid_team)))
        return teams.scalars().all()


team = CRUDTeam(Team)
