import os
import json

from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
admins_id_str = os.getenv('ADMINS_ID', [])
try:
    ADMINS = json.loads(admins_id_str)
    print(ADMINS[0])
except json.JSONDecodeError:
    print("Ошибка декодирования JSON")
    admins_id_list = []


DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку"),
    ('get_promo', 'Получить промокод'),
)

ADMINS_COMMANDS = (
    ('count', "Количество оставшихся промокодов"),
    ('loud_pr', "Загрузить промокоды"),
    ('set_time', 'Установить время окончания раздачи'),
    ('reset ', 'Обнулить промокоды'),
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
