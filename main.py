import asyncio
from tortoise import Tortoise

import handlers
from loader import dp, bot
from config.settings import TORTOISE_ORM
from logs.logger import LoggerSetup
from handlers.commands.info import start_bot, stop_bot
from handlers.commands import commands_handler, admins_handler




async def on_startup():
    # Настройка логирования
    logger_setup = LoggerSetup(logger_name='bot_logger')
    logger = logger_setup.logger
    logger.info("Старт бота")

    # Настройка Tortoise ORM
    await Tortoise.init(config=TORTOISE_ORM)
    await Tortoise.generate_schemas()
    await start_bot()
    dp.include_routers(commands_handler.router)
    dp.include_routers(admins_handler.router)




async def start():
    try:
        dp.startup.register(on_startup)

        dp.shutdown.register(stop_bot)
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())
