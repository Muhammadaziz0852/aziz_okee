from aiogram.fsm.state import State, StatesGroup


class EmailState(StatesGroup):
    subject = State()
    description = State()
    send_time = State()

