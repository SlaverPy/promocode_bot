from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChatAdministrators
from config.settings import DEFAULT_COMMANDS, ADMINS_COMMANDS, ADMINS


async def set_commands(bot: Bot):
    commands = [BotCommand(command=command, description=descriptions) for command, descriptions in DEFAULT_COMMANDS]

    await bot.set_my_commands(commands, BotCommandScopeDefault())
