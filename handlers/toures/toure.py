from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    Message,
    CallbackQuery,
)
from aiogram.filters.command import Command

from keyboards.create_inline_keyboard import create_inline_keyboard
from states.toure_6_less import ToureStates
from utils.toures import get_data

router = Router()


def get_prev_data(dict: dict):
    result = []
    for key, value in dict.items():
        result.append(value)

    print("Прошлые данные -> ", result)
    return result


@router.message(Command("application"))
async def cmd_test_2(message: Message, state: FSMContext):
    keyboard = await create_inline_keyboard(get_data(0, []))
    await state.set_state(ToureStates.Counting)
    await message.answer(
        "Сколько человек собирается учавствовать в туре?",
        reply_markup=keyboard.as_markup(),
    )


@router.callback_query(ToureStates.Counting)
async def cmd_counting(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(counting=callback_query.data)
    await state.set_state(ToureStates.TourePlace)
    keyboard = await create_inline_keyboard(get_data(1, get_prev_data(data)))
    # keyboard = await create_inline_keyboard(
    #     [
    #         {"text": "hello", "callback_data": "1"},
    #         {"text": "world", "callback_data": "2"},
    #     ]
    # )
    await callback_query.message.answer(
        "Выберите тур", reply_markup=keyboard.as_markup()
    )
    # await callback_query.message.answer("hello")


@router.callback_query(ToureStates.TourePlace)
async def cmd_toure_place(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(toure_place=callback_query.data)
    await state.set_state(ToureStates.ToureEnd)
    keyboard = await create_inline_keyboard(
        get_data(2, [data["counting"], callback_query.data])
    )
    await callback_query.message.answer(callback_query.data, reply_markup=keyboard)
