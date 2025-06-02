from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, Contact
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from keyboards.send_number import create_contact_keyboard
from keyboards.create_inline_keyboard import create_inline_keyboard
from states.toure_6_less import ToureStates
from utils.toures import find_callback_data
from utils.tour_data import TOUR_STRUCTURE

router = Router()


def get_prev_data(dict: dict):
    result = []
    for key, value in dict.items():
        result.append(value)

    print("Прошлые данные -> ", result)
    return result


@router.message(Command("application"))
async def cmd_test_2(message: Message, state: FSMContext):
    keyboard = await create_inline_keyboard(TOUR_STRUCTURE(0, []))
    await state.set_state(ToureStates.Counting)
    await message.answer(
        "Сколько человек собирается учавствовать в туре?", reply_markup=keyboard
    )


@router.callback_query(ToureStates.Counting)
async def counting(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(counting=callback_query.data)
    await state.set_state(ToureStates.TourePlace)
    keyboard = await create_inline_keyboard(TOUR_STRUCTURE(1, get_prev_data(data)))
    await callback_query.answer("Done!")
    await callback_query.message.answer("Выберите тур", reply_markup=keyboard)


@router.callback_query(ToureStates.TourePlace)
async def toure_place(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(toure_place=callback_query.data)
    await state.set_state(ToureStates.ToureEnd)

    keyboard = await create_inline_keyboard(TOUR_STRUCTURE(2, get_prev_data(data)))
    await callback_query.answer("Done!")

    await callback_query.message.answer("Выберите тур снова!", reply_markup=keyboard)
    await state.set_state(ToureStates.ToureEnd)


@router.callback_query(ToureStates.ToureEnd)
async def get_number(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(toure_end=callback_query.data)
    keyboard = await create_contact_keyboard()
    await callback_query.answer("Done!")
    await callback_query.message.answer(
        "Поделитесь своими контактами", reply_markup=keyboard
    )
    await state.set_state(ToureStates.Contact)
    # await state.clear()


@router.message(F.content_type == "contact", ToureStates.Contact)
async def toure_end(message: Message, state: FSMContext):
    data = await state.get_data()
    print(data)
    prev_data = get_prev_data(data)
    result = find_callback_data(prev_data)
    name = ""
    tg_username = message.from_user.username
    if message.contact.first_name is not None:
        name += message.contact.first_name
        if message.contact.last_name is not None:
            name += " " + message.contact.last_name
    format_data = (
        f"<b>Пришел запрос на тур:</b> \n\n"
        f"Количество человек в туре: {result[0]} \n\n"
        f"Тур в котором пришли: {result[1]} \n\n"
        f"Место тура: {result[2]}\n\n"
        f"ФИО: {name} \n\n"
        f"Телефон: {message.contact.phone_number} \n\n"
        f"Telegram: @{tg_username}"
    )

    await message.answer(format_data, parse_mode="HTML")

    await state.clear()
