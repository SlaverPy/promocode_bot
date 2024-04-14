from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_yes_no_buttons():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="Да", callback_data="yes"),
        InlineKeyboardButton(text="Нет", callback_data="no"),
    ]])

    return keyboard
