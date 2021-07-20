from typing import Optional

from pydantic import BaseModel
from pydantic.types import UUID4

# Shared properties
class AwardsBase(BaseModel):
    uuid_team: UUID4
    uuid_award_type: UUID4
    comment: str


# Properties to receive via API on creation
class AwardsCreate(AwardsBase):
    pass


# Properties to receive via API on update
class AwardsUpdate(AwardsBase):
    pass


class AwardsInDBBase(AwardsBase):
    uuid: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class Awards(AwardsInDBBase):
    pass


# Additional properties stored in DB
class AwardsInDB(AwardsInDBBase):
    pass


# Shared properties
class AwardTypesBase(BaseModel):
    name: str
    being_given: int
    description: str


# Properties to receive via API on creation
class AwardTypesCreate(AwardTypesBase):
    pass


# Properties to receive via API on update
class AwardTypesUpdate(AwardTypesBase):
    pass


class AwardTypesInDBBase(AwardTypesBase):
    uuid: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class AwardTypes(AwardTypesInDBBase):
    pass


# Additional properties stored in DB
class AwardTypesInDB(AwardTypesInDBBase):
    pass
