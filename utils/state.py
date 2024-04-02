from aiogram.fsm.state import State, StatesGroup


class PromoCodeState(StatesGroup):
    waiting_for_promocodes = State()
    set_time_for_promocodes = State()
    reset_promocodes = State()

