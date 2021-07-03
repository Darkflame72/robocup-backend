from typing import List
from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

from .team_member import TeamMember
from .team_member import TeamMemberBase

# Shared properties
class TeamBase(BaseModel):
    name: str
    organisation: str
    hardware_type: str
    software_type: str
    uuid_mentor: UUID4
    uuid_competition: UUID4


# Properties to receive via API on creation
class TeamCreate(TeamBase):
    team_members: List[TeamMemberBase]


# Properties to receive via API on update
class TeamUpdate(TeamBase):
    pass


class TeamInDBBase(TeamBase):
    uuid: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Team(TeamInDBBase):
    num_member: int
    team_present: int = 0
    interview_comments: Optional[str] = None


class TeamApi(Team):
    team_members: List[TeamMember]


# Additional properties stored in DB
class TeamInDB(TeamInDBBase):
    pass
