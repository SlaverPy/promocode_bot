from loader import bot
from .commands import set_commands
from config.settings import ADMINS


async def start_bot():
    await set_commands(bot)
    for admin in ADMINS:
        await bot.send_message(admin, 'Бот запущен')


async def stop_bot():
    for admin in ADMINS:
        await bot.send_message(admin, 'остановлен')
