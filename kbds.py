from typing import Tuple
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_keyboard(
    *btns,
    placeholder: str = None,
    sizes: Tuple[int] = (2,),
):
    keyboard = ReplyKeyboardBuilder()
    for btn in btns:
        keyboard.add(KeyboardButton(text=btn))

    return keyboard.adjust(*sizes).as_markup(resize_keyboard=True, input_field_placeholder=placeholder)