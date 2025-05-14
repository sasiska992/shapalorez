from aiogram.fsm.state import StatesGroup, State


class ToureStates(StatesGroup):
    Counting = State()
    TourePlace = State()
    ToureEnd = State()



