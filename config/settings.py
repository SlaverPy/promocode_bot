import os
import json

from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
admins_id_str = os.getenv('ADMINS_ID', [])
INFO_GROUP = os.getenv('INFO_GROUP', [])

try:
    ADMINS = json.loads(admins_id_str)
except json.JSONDecodeError:
    print("Ошибка декодирования JSON")
    admins_id_list = []


DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Не получил промокод, что делать?"),
    ('get_promo', 'Получить промокод'),
)

ADMINS_COMMANDS = (
    ('count', "Количество оставшихся промокодов"),
    ('loud_pr', "Загрузить промокоды"),
    ('set_time', 'Установить время раздачи'),
    ('reset ', 'Обнулить промокоды'),
    ('start_dist ', 'Начать раздача промокодов'),
)

TORTOISE_ORM = {
    "connections": {"default": "sqlite://database/db/db.sqlite3"},
    "apps": {
        "models": {
            "models": ["database.model"],
            "default_connection": "default",
        },
    },
}
