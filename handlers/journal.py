from aiogram import Router, types
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import sessionmaker
from filters.isRegistered import IsRegistered


journal_router = Router()

@journal_router.message('Электронный журнал', IsRegistered(sessionmaker()))
async def start_journal(mess: types.Message, session: AsyncSession):
    pass