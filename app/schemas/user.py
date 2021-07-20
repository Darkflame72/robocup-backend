from typing import Optional

from pydantic import BaseModel
from pydantic import EmailStr
from pydantic.types import UUID4

# Shared properties
class UserBase(BaseModel):
    email: EmailStr
    is_superuser: bool = False
    full_name: str
    is_active: bool = True
    phone_number: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    uuid: Optional[UUID4] = None

    class Config:
        orm_mode = True


# Additional properties to return via API
class User(UserInDBBase):
    pass


# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
