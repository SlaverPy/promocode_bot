from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


from config.settings import DEFAULT_COMMANDS, ADMINS_COMMANDS, ADMINS

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
