import uuid

from app.db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import Text
from sqlalchemy import DateTime
from sqlalchemy import Time
from sqlalchemy import String
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID


class rescue_round_type(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("round_type", String(50), nullable=False),
    Column("sort_order", Integer(), nullable=False),


class rescue_round(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("uuid_rescue_round_type", UUID(as_uuid=True), nullable=False),
    Column("uuid_challenge_division", UUID(as_uuid=True), nullable=False),
    Column("max_time", String(13), nullable=False),


class rescue_course_setups(Base):
    Column("uuid_rescue_round", UUID(as_uuid=True), nullable=False),
    Column("level0", Text(), nullable=False),
    Column("level1", Text(), nullable=False),
    Column("level0_starts", Text(), nullable=False),
    Column("level1_starts", Text(), nullable=False),
    Column("level0_capsules", Text(), nullable=False),
    Column("level1_capsules", Text(), nullable=False),
    Column("ramps", Text(), nullable=False),
    Column("comments", Text(), nullable=True),


class rescue_result(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("uuid_rescue_round", UUID(as_uuid=True), nullable=False),
    Column("uuid_team", UUID(as_uuid=True), nullable=False),
    Column("uuid_referee", UUID(as_uuid=True), nullable=False),
    Column("gross_time", Time, nullable=False),
    Column("touch", Integer(), nullable=False),
    Column("timestamp", DateTime, default=datetime()),
    Column("total_raw_score", Integer(), nullable=False, default=0),
    Column("referee", UUID(as_uuid=True), nullable=False),
    Column("approval_type", Integer(), nullable=True),
    Column("dnc", Integer(), nullable=False),
    Column("comment", String(1000), nullable=True),
    Column("status", String(50), nullable=False),


class rescue_result_tile(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("uuid_rescue_result", UUID(as_uuid=True), nullable=False),
    Column("uuid_tile_round", UUID(as_uuid=True), nullable=False),
    Column("points_a", Integer(), nullable=False, default=0),
    Column("points_b", Integer(), nullable=False, default=0),
    Column("points_c", Integer(), nullable=False, default=0),
    Column("points_d", Integer(), nullable=False, default=0),
    Column("points_e", Integer(), nullable=False, default=0),
    Column("points_f", Integer(), nullable=False, default=0),
    Column("points_g", Integer(), nullable=False, default=0),
    Column("points_h", Integer(), nullable=False, default=0),
    Column("points_i", Integer(), nullable=False, default=0),
    Column("points_j", Integer(), nullable=False, default=0),


class rescue_tile(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("tile_name", String(50), nullable=False),
    Column("tile_description", Text(), nullable=False),
    Column("image_name", Text, nullable=False),
    Column("points_a", Integer(), nullable=False),
    Column("points_b", Integer(), nullable=False),
    Column("points_c", Integer(), nullable=False),
    Column("points_d", Integer(), nullable=False),
    Column("points_e", Integer(), nullable=False),
    Column("points_f", Integer(), nullable=False),
    Column("points_g", Integer(), nullable=False),
    Column("points_h", Integer(), nullable=False),
    Column("points_i", Integer(), nullable=False),
    Column("points_j", Integer(), nullable=False),
    Column("tile_rule", String(16), nullable=False),
    Column("tags", String(400), nullable=False),
    Column("hidden", Integer(), nullable=False),
    Column("is_child", Integer(), nullable=False),
    Column("parent_debris", String(16), nullable=False),
    Column("parent_obstacle", String(16), nullable=False),
    Column("scoring_tips", Text(), nullable=False),


class rescue_tile_tag(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("name", String(64), nullable=False),


class rescue_tile_round(Base):
    Column("uuid", UUID(as_uuid=True), nullable=False, default=uuid.uuid4()),
    Column("uuid_rescue_round", UUID(as_uuid=True), nullable=False),
    Column("uuid_rescue_tile", UUID(as_uuid=True), nullable=False),
