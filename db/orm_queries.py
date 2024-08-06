from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User


async def get_all_ids(session: AsyncSession):
    q = select(User.id)
    data = await session.execute(q)
    return data.scalars().all()