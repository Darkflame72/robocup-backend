import datetime
from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

# Shared properties
class OnstageInterviewBase(BaseModel):
    uuid_team: UUID4
    status: str
    score: int
    data: str
    comment: str
    timestamp: datetime
    uuid_onstage_round: str
    uuid_ref: str


# Properties to receive via API on creation
class OnstageInterviewCreate(OnstageInterviewBase):
    pass


# Properties to receive via API on update
class OnstageInterviewUpdate(OnstageInterviewBase):
    pass


class OnstageInterviewInDBBase(OnstageInterviewBase):
    uuid: Optional[UUID4] = None
    dnc: bool

    class Config:
        orm_mode = True


# Additional properties to return via API
class OnstageInterview(OnstageInterviewInDBBase):
    pass


# Additional properties stored in DB
class OnstageInterviewInDB(OnstageInterviewInDBBase):
    pass
