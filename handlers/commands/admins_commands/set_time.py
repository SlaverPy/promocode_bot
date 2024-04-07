from aiogram import Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext

from utils.state import PromoCodeState
from config.settings import ADMINS
from keybords import time_for_start

router = Router()

@router.message(Command(commands=["set_time"]))
async def set_time_promocode(message: types.Message, state: FSMContext):
    if message.from_user.id in ADMINS:
        await message.answer("Выберите время", reply_markup=time_for_start())

        await state.set_state(PromoCodeState.start_time)

@router.callback_query(StateFilter(PromoCodeState.start_time))
async def process_start_time(callback_query: types.CallbackQuery, state: FSMContext):
    if callback_query.from_user.id in ADMINS:
        print(callback_query)
    print("нет id")

# @router.callback_query(state=PromoCodeState.end_time)
# async def process_end_time(callback_query: types.CallbackQuery, state: FSMContext):
#     ...
