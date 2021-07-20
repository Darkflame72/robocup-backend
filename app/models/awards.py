import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import text
from sqlalchemy import Integer
from sqlalchemy.dialects.postgresql import UUID


class AwardTypes(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, primary_key=True)
    Column("name", Text, nullable=False)
    # Column("for_challenge", Text, nullable=False),
    Column("being_given", Integer, nullable=False)
    Column("description", Text, default=text("NULL"))


class Awards(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False)
    # Column("uuid_challenge_division", UUID(as_uuid=True), nullable=False),
    Column("uuid_team", UUID(as_uuid=True), nullable=False)
    Column("uuid_award_type", UUID(as_uuid=True), nullable=False)
    Column("comment", Text, server_default=text("NULL"))
