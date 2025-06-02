from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from keyboards.send_number import create_contact_keyboard
from keyboards.create_inline_keyboard import (
    create_inline_keyboard_for_toures_with_button_go_back,
)
from states.toure_6_less import ToureStates
from utils.toures import get_next_values, get_prev_data
from utils.format_final_message import format_final_message

from aiogram.types import ReplyKeyboardRemove

router = Router()


@router.message(Command("application"))
async def cmd_test_2(message: Message, state: FSMContext):
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(0, []), "help"
    )
    await state.set_state(ToureStates.Counting)
    await message.answer(
        "Сколько человек собирается учавствовать в туре?", reply_markup=keyboard
    )


@router.callback_query(ToureStates.Counting)
async def counting(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(counting=callback_query.data)
    await state.set_state(ToureStates.TourePlace)
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(1, get_prev_data(data)), "counting_back"
    )
    await callback_query.answer("")
    await callback_query.message.answer(
        "Отлично, теперь давайте выберем поездку!", reply_markup=keyboard
    )


@router.callback_query(ToureStates.TourePlace)
async def toure_place(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(toure_place=callback_query.data)
    await state.set_state(ToureStates.ToureEnd)

    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(2, get_prev_data(data)), "toure_place_back"
    )
    await callback_query.answer("")

    await callback_query.message.answer("Выберите тур снова!", reply_markup=keyboard)
    await state.set_state(ToureStates.ToureEnd)


@router.callback_query(ToureStates.ToureEnd)
async def get_number(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(toure_end=callback_query.data)
    keyboard = await create_contact_keyboard()
    await callback_query.answer("")
    await callback_query.message.answer(
        "Поделитесь своими контактами", reply_markup=keyboard
    )
    await state.set_state(ToureStates.Contact)
    # await state.clear()


@router.message(F.content_type == "contact", ToureStates.Contact)
async def toure_end(message: Message, state: FSMContext):
    data = await state.get_data()

    await message.answer(
        format_final_message(message, data),
        parse_mode="HTML",
        reply_markup=ReplyKeyboardRemove(),
    )

    await state.clear()
