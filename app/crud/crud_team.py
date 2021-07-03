from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from uuid import uuid4

from app.crud.base import CRUDBase
from app.models.team import Team
from app.models.team import TeamMember
from app.schemas.team import TeamCreate
from app.schemas.team import TeamUpdate
from pydantic.types import UUID4
from sqlalchemy.orm import Session


class CRUDTeam(CRUDBase[Team, TeamCreate, TeamUpdate]):
    def create(self, db: Session, *, obj_in: TeamCreate) -> Team:
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
        db.add(db_obj)
        db.commit()
        for member in obj_in.team_members:
            mem_obj = TeamMember(
                uuid=member.uuid, uuid_team=db_obj.uuid, role=member.role
            )
            db.add(mem_obj)
            db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_team_members(self, db: Session, uuid: UUID4) -> List[TeamMember]:
        return db.query(TeamMember).filter(TeamMember.uuid_team == uuid).all()

    def update(
        self, db: Session, *, db_obj: Team, obj_in: Union[TeamUpdate, Dict[str, Any]]
    ) -> Team:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return super().update(db, db_obj=db_obj, obj_in=update_data)


team = CRUDTeam(Team)
