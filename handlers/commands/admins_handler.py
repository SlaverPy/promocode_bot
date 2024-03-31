from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


from config.settings import ADMINS_COMMANDS, ADMINS

router = Router()

@router.message(Command(commands=["count"]))
async def loud_promocode(message: Message):
    if message.from_user.id in ADMINS:
        print(1)


@router.message(Command(commands=["loud_pr"]))
async def loud_promocode(message: Message):
    if message.from_user.id in ADMINS:
        print(2)


@router.message(Command(commands=["set_time"]))
async def loud_promocode(message: Message):
    if message.from_user.id in ADMINS:
        print(3)
