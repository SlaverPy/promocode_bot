from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from database.model import Promocods
from utils.state import PromoCodeState
from config.settings import ADMINS

router = Router()

@router.message(Command(commands=["count"]))
async def count_promocode(message: Message):
    if message.from_user.id in ADMINS:
        active_promocodes_count = await Promocods.filter(is_active=True).count()
        await message.answer(f"Общее количество активных промокодов: {active_promocodes_count}")


@router.message(Command(commands=["loud_pr"]))
async def loud_promocode(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Пожалуйста, введите промокоды, каждый с новой строки."
                             " Когда закончите, отправьте команду /stop.")
        await state.set_state(PromoCodeState.waiting_for_promocodes)


@router.message(PromoCodeState.waiting_for_promocodes)
async def get_promocodes(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        promocodes = message.text.split('\n')
        for code in promocodes:
            # Здесь код для добавления каждого промокода в базу данных
            await Promocods.create(promocode=code, is_active=True)
        active_promocodes_count = await Promocods.filter(is_active=True).count()
        await message.answer(f"Промокоды успешно загружены. Общее количество активных промокодов: {active_promocodes_count}")
        await state.clear()


@router.message(Command(commands=["set_time"]))
async def loud_promocode(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        active_promocodes_count = await Promocods.filter(is_active=True).count()
        await message.answer(f"Общее количество активных промокодов: {active_promocodes_count}")
        await message.answer(f"Для подтверждения отправьте 'Да'")
        await state.set_state(PromoCodeState.reset_promocodes)


@router.message(PromoCodeState.reset_promocodes)
async def reset_promocodes(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        if message.text.lower() == 'да':
            await Promocods.all().update(is_active=False)
            await state.clear()
            await message.answer(f"Промокоды сброшены")
