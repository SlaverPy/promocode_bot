from aiogram import Bot, Dispatcher

from config import settings

bot = Bot(token=settings.BOT_TOKEN, parse_mode='HTML')
dp = Dispatcher()



