import datetime

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from config.settings import ADMINS
from database.model import Promocods, BotUser
from config.settings import DEFAULT_COMMANDS, ADMINS_COMMANDS, ADMINS
from database.model import DistributionTime
router = Router()


@router.message(Command(commands=["start"]))
async def start_command(message: Message):
    print("start_command")
    commands = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    admin_commands = [f'/{command} - {desk}' for command, desk in ADMINS_COMMANDS]
    if message.from_user.id in ADMINS:
        commands_text = "\n".join(commands + admin_commands)
    else:
        commands_text = "\n".join(commands)
    await message.answer(f"Доступные команды:\n{commands_text}")


@router.message(Command(commands=["get_promo"]))
async def start_command(message: Message):
    user_id = message.from_user.id
    current_user = await BotUser.filter(user_id=user_id).first()
    now = datetime.datetime.now()

    # Проверяем, есть ли активный период распределения промокодов
    active_distribution = await DistributionTime.filter(time_start__lte=now, time_end__gte=now).first()

    if active_distribution:
        if current_user.can_get_code or user_id in ADMINS:
            active_promocode = await Promocods.filter(is_active=True).first()
            if active_promocode:
                await message.answer(f"Ваш промокод: {active_promocode}.")
                current_user.can_get_code = False
                await current_user.save()
            else:
                await message.answer("Извините, но промокоды закончились, следите за обновлением в чате.")
        else:
            await message.answer(f"Вы уже получали промокод в текущей раздаче.")
    else:
        await message.answer("Извините, но в текущий момент недоступны промокоды.")

