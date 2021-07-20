from typing import Any
from typing import Dict
from typing import List
from typing import Optional
from typing import Union
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from app.crud.base import CRUDBase
from app.models.awards import Awards
from app.models.awards import AwardsMember
from app.schemas.awards import AwardsCreate
from app.schemas.awards import AwardsUpdate
from pydantic.types import UUID4


class CRUDAwards(CRUDBase[Awards, AwardsCreate, AwardsUpdate]):
    async def create(self, db: AsyncSession, *, obj_in: AwardsCreate) -> Awards:
        db_obj = Awards(
            uuid=uuid4(),
            name=obj_in.name,
            organisation=obj_in.organisation,
            num_member=len(obj_in.team_members),
            uuid_mentor=obj_in.uuid_mentor,
            hardware_type=obj_in.hardware_type,
            software_type=obj_in.software_type,
            uuid_competition=obj_in.uuid_competition,
        )
        await db.add(db_obj)
        await db.commit()
        for member in obj_in.team_members:
            mem_obj = AwardsMember(
                uuid=uuid4(),
                uuid_user=member.uuid,
                uuid_team=db_obj.uuid,
                role=member.role,
            )
            await db.add(mem_obj)
        await db.commit()
        db.refresh(db_obj)
        return db_obj

    async def update(
        self, db: AsyncSession, *, db_obj: Awards, obj_in: Union[AwardsUpdate, Dict[str, Any]]
    ) -> Awards:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        return await super().update(db, db_obj=db_obj, obj_in=update_data)



team = CRUDAwards(Awards)
