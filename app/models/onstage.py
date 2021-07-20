import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import String
from sqlalchemy import JSON
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class onstage_round_type(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("round_name", String(50), nullable=False)
    Column("round_type", String(50), nullable=False)
    Column("sort_order", Integer, nullable=False)


class onstage_round(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("uuid_onstage_round_type", UUID(as_uuid=True), nullable=False)
    Column("uuid_challenge_division", UUID(as_uuid=True), nullable=False)


class onstage_interview(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("uuid_team", UUID(as_uuid=True), nullable=False)
    Column("competition", Integer, nullable=False)
    Column("score", Integer, nullable=False)
    Column("data", JSON, nullable=False)
    Column("comment", Text, nullable=True)
    Column("timesamp", DateTime, nullable=False, default=datetime.now())


class onstage_performance(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("uuid_team", UUID(as_uuid=True), nullable=False)
    Column("status", String(64), server_default=None)
    Column("score", String(32), nullable=False)
    Column("data", String(1028), nullable=False)
    Column("comment", String(1000), server_default=None)
    Column("timestamp", DateTime, nullable=False, default=datetime.now())
    Column("uuid_onstage_round", UUID(as_uuid=True), nullable=False)
    Column("uuid_user", UUID(as_uuid=True), nullable=False)
    Column("dnc", Integer, nullable=False)


class onstage_scoresheet_categories(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("type", String(13), nullable=False)
    Column("division", String(13), nullable=False)
    Column("name", String(256), nullable=False)
    Column("step", String(16), nullable=False, default=1)
    Column("sort_order", String(8), nullable=False)


class onstage_scoresheet_criteria(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("descriptor", String(13), nullable=False)
    Column("name", String(256), nullable=False)
    Column("points", String(64), nullable=False)


class onstage_scoresheet_descriptors(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4())
    Column("category", String(13), nullable=False)
    Column("name", String(256), nullable=False)
    Column("sort_order", String(8), nullable=False)
