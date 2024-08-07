from aiogram import F, Router, types
from aiogram.filters import StateFilter
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode
from sqlalchemy.ext.asyncio import AsyncSession
from db.engine import sessionmaker
from db.orm_queries import create_user, get_user
from filters.isRegistered import IsRegistered
import hashlib

from kbds import get_keyboard
from services.auth import auth
from services.get_guid import get_guid
from services.get_marks import get_marks
from utils.crypter import decrypt, encrypt
from utils.get_session import get_session

journal_router = Router()

class UserState(StatesGroup):
    login = State()
    password = State()

    token = State()

@journal_router.message(F.text == 'Электронный журнал', IsRegistered(sessionmaker()))
async def start_journal(mess: types.Message, session: AsyncSession, state: FSMContext):
    user_state = await state.get_data()
    if not user_state['token']:
        await start_register(mess, session, state)
        return

    user_data = await get_user(mess.from_user.id, session)
    token = await auth(user_data.login, decrypt(user_data.password))
    await state.update_data(token=token)

    await mess.answer('Электронный журнал:')

@journal_router.message(F.text == 'Электронный журнал', StateFilter(None))
async def start_register(mess: types.Message, state: FSMContext):
    await mess.answer('Введи почту или снилс:')
    await state.set_state(UserState.login)

@journal_router.message(F.text == 'Оценки')
async def marks(mess: types.Message, session: AsyncSession, state: FSMContext):
    token = (await state.get_data())['token']
    user_data = await get_user(mess.from_user.id, session)
    marks = get_marks(get_session(token), user_data.guid)

    print(marks)


@journal_router.message(UserState.login, F.text)
async def add_login(mess: types.Message, state: FSMContext):
    await state.update_data(login=mess.text)
    await mess.answer('Введи пароль:')
    await state.set_state(UserState.password)

@journal_router.message(UserState.password, F.text)
async def add_password(mess: types.Message, state: FSMContext, session: AsyncSession):
    await state.update_data(password=mess.text)
    user_data = await state.get_data()

    token, session = auth(user_data['login'], user_data['password'])
    await state.update_data(token=token)
    await state.clear()

    user_data['uid'] = mess.from_user.id
    user_data['guid'] = get_guid(session)
    await create_user(user_data, session)

    await mess.answer('<b>Вы зарегистрированы</b>', 
                      parse_mode=ParseMode.HTML, 
                      reply_markup=get_keyboard('Дневник', 'Оценки'))