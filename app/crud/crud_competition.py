import datetime
from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from uuid import uuid4

from app.crud.base import CRUDBase
from app.models.competition import Competition
from app.models.team import TeamMember
from app.schemas.competition import CompetitionCreate
from app.schemas.competition import CompetitionUpdate
from app.schemas.team import Team
from app.schemas.team import TeamApi
from pydantic.types import UUID4
from sqlalchemy.orm import Session

from .crud_team import team


class CRUDCompetition(CRUDBase[Competition, CompetitionCreate, CompetitionUpdate]):
    def get_by_date(self, db: Session, *, date: datetime.date) -> Optional[Competition]:
        return db.query(Competition).filter(Competition.date == date).first()

    def create(self, db: Session, *, obj_in: CompetitionCreate) -> Competition:
        db_obj = Competition(
            uuid=uuid4(), name=obj_in.name, region=obj_in.region, date=obj_in.date,
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    def get_competition_teams(self, db: Session, uuid: UUID4) -> List[TeamMember]:
        base_teams = db.query(Team).filter(Team.uuid_competition == uuid).all()
        teams = []
        for _team in base_teams:
            teams.append(
                TeamApi(
                    **_team.__dict__, team_members=team.get_team_members(db, _team.uuid)
                )
            )
        return teams


competition = CRUDCompetition(Competition)
