from aiogram.fsm.state import StatesGroup, State


class ToureStates(StatesGroup):
    Counting = State()
    TourePlace = State()
    ToureDate = State()
    Contact = State()
    ToureEnd = State()



