from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from db.models import User
from schemas.user import User as UserSchema
from utils.crypter import encrypt


async def get_all_ids(session: AsyncSession):
    q = select(User.uid)
    data = await session.execute(q)
    return data.scalars().all()

async def create_user(user_data: UserSchema, session: AsyncSession):
    obj = User(
        uid = user_data['uid'],
        password = user_data['password']
    )

    session.add(obj)
    await session.commit()

async def get_user(uid: str, session: AsyncSession):
    q = select(User).where(User.uid == uid)
    data = await session.execute(q)
    user = data.scalar()

    return user