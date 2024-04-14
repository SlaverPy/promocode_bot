from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.model import Promocods
from utils.state import PromoCodeState
from config.settings import ADMINS
from keybords.yes_no_keybords import get_yes_no_buttons

router = Router()


@router.message(Command(commands=["reset"]))
async def loud_promocode(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Вы уверены, что хотите обнулить промокоды?")
        keyboard = get_yes_no_buttons()
        await message.reply_text("Выберите действие:", reply_markup=keyboard)
        await state.set_state(PromoCodeState.reset_promocodes)


@router.callback_query(lambda c: c.data in ["yes", "no"], state=PromoCodeState.reset_promocodes)
async def on_callback_query(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.from_user.id in ADMINS:
        if callback_query.data == "yes":
            # Предполагается, что Promocods - это ваша модель Tortoise ORM
            await Promocods.all().update(is_active=False)
            await callback_query.answer("Промокоды сброшены")
            await state.clear()
        elif callback_query.data == "no":
            await callback_query.answer("Вы выбрали 'нет'")
            await state.clear()
