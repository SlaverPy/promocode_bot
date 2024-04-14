import datetime

from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from utils.state import PromoCodeState
from utils.info_bot_status import seng_start_to_info_group
from config.settings import ADMINS
from keybords import time_for_start
from database.model import DistributionTime, Promocods

router = Router()


@router.message(Command(commands=["set_time"]))
async def set_time_promocode(message: Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Выберите время", reply_markup=time_for_start())

        await state.set_state(PromoCodeState.start_time)


@router.callback_query(StateFilter(PromoCodeState.start_time))
async def process_start_time(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.from_user.id in ADMINS:
        print(callback_query)
    print("нет id")


@router.message(Command(commands=["start_dist"]))
async def start_distribution_promocodes(message: Message):
    if message.from_user.id in ADMINS:
        active_promocodes_count = await Promocods.filter(is_active=True).count()
        if active_promocodes_count > 0:
            await update_distribution_time()
            await seng_start_to_info_group()
            await message.answer(f"раздача началась, на данный момент доступно: {active_promocodes_count} промокодов")
        else:
            await message.answer(f"Нет доступных промокодов для начала раздачи")


async def update_distribution_time(current_time=datetime.datetime.now(),
                                   time_end=datetime.datetime.now() + datetime.timedelta(hours=3)):
    distribution_time = await DistributionTime.all().order_by('-create_at').first()

    if distribution_time:
        await distribution_time.update_from_dict({"time_start": current_time, "time_end": time_end})
        print("Запись обновлена.")
    else:
        await DistributionTime.create(time_start=current_time, time_end=time_end)
        print("Новая запись создана.")
