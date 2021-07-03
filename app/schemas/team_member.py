from typing import List
from typing import Optional

from app.schemas.user import User
from pydantic import BaseModel
from pydantic.types import UUID4

# Shared properties
class TeamMemberBase(BaseModel):
    uuid: UUID4
    role: str


# Properties to receive via API on creation
class TeamMemberCreate(TeamMemberBase):
    uuid_team: UUID4


# Properties to receive via API on update
class TeamMemberUpdate(TeamMemberBase):
    uuid_team: UUID4


class TeamMemberInDBBase(TeamMemberBase):
    uuid_team: UUID4

    class Config:
        orm_mode = True


# Additional properties to return via API
class TeamMember(TeamMemberInDBBase):
    uuid_team: UUID4


# Additional properties stored in DB
class TeamMemberInDB(TeamMemberInDBBase):
    pass
