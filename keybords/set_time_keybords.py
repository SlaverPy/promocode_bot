from datetime import datetime, timedelta
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def time_for_start():
    now = datetime.now()
    next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
    next_two_hours = (now + timedelta(hours=2)).replace(minute=0, second=0, microsecond=0)
    next_three_hours = (now + timedelta(hours=3)).replace(minute=0, second=0, microsecond=0)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Сейчас", callback_data=f"{now}"),
        InlineKeyboardButton(text="Через час", callback_data=f"{next_hour}"),
        InlineKeyboardButton(text="Через 2 часа", callback_data=f"{next_two_hours}"),
        InlineKeyboardButton(text="Через 3 часа", callback_data=f"{next_three_hours}"),
        InlineKeyboardButton(text="Ввести время", callback_data="input")
    ]])

    return keyboard
