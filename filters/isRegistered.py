from aiogram.filters import Filter
from aiogram import types
from sqlalchemy.ext.asyncio import AsyncSession

from db.orm_queries import get_all_ids

class IsRegistered(Filter):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def __call__(self, mess: types.Message):
        ids = await get_all_ids(self.session)
        return mess.from_user.id in ids