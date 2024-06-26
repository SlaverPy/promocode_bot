from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.model import Promocods
from utils.state import PromoCodeState
from config.settings import ADMINS

router = Router()


@router.message(Command(commands=["loud_pr"]))
async def loud_promocode(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Пожалуйста, введите промокоды, каждый с новой строки.")
        await state.set_state(PromoCodeState.waiting_for_promocodes)


@router.message(PromoCodeState.waiting_for_promocodes)
async def get_promocodes(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        promocodes = message.text.split('\n')
        for code in promocodes:
            # Здесь код для добавления каждого промокода в базу данных
            await Promocods.create(promocode=code, is_active=True)
        active_promocodes_count = await Promocods.filter(is_active=True).count()
        await message.answer(
            f"Промокоды успешно загружены. Общее количество активных промокодов: {active_promocodes_count}")
        await state.clear()

