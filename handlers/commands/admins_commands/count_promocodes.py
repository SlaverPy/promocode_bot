from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from database.model import Promocods
from config.settings import ADMINS


router = Router()


@router.message(Command(commands=["count"]))
async def get_count_promocode(message: Message):
    if message.from_user.id in ADMINS:
        promocodes_count = await Promocods.all().count()
        active_promocodes_count = await Promocods.filter(is_active=True).count()

        await message.answer(f"Общее количество активных промокодов: {active_promocodes_count}\n"
                             f"Всего промокодов: {promocodes_count}")
