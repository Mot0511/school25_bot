import asyncio
import os
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from dotenv import find_dotenv, load_dotenv
from kbds import get_keyboard
from handlers.journal import journal_router
from middlewares.db_session import DBSession
from db.engine import sessionmaker

load_dotenv(find_dotenv())

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()

@dp.message(CommandStart())
async def start(mess: types.Message):
    await mess.answer('<b>Привет!</b> Это бот школы 25 города Кирова\n\n<b>Здесь ты можешь:</b>\n- посмотреть оценки или дз из электронного дневника\n- посмотреть расписание уроков или звонков\n- узнать сколько минут до урока или перемены', 
                        parse_mode=ParseMode.HTML, 
                        reply_markup=get_keyboard('Электронный журнал', 'Расписание уроков', 'Расписание звонков', 'Сколько минут до урока/перемены')
                      )

dp.include_router(journal_router)

async def main():
    dp.update.middleware(DBSession(sessionmaker))
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())