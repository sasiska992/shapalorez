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
import random


import asyncio


from aiogram.types import ReplyKeyboardRemove

from handlers.help import cmd_help

router = Router()


@router.message(Command("application"))
async def cmd_application(message: Message, state: FSMContext):
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(0, []), "toures_application_help"
    )
    await state.set_state(ToureStates.Counting)
    await message.answer(
        "👋 Привет! Сколько человек планируют участвовать в туре? Выберите вариант ниже:",
        reply_markup=keyboard,
    )


# Возвращает пользователя в случае необходимости в команду /help
@router.callback_query(ToureStates.Counting, F.data == "toures_application_help")
async def application_help(callback_query: CallbackQuery, state: FSMContext):
    await cmd_help(callback_query.message)
    await callback_query.answer("")
    await state.clear()


@router.callback_query(ToureStates.Counting)
async def counting(callback_query: CallbackQuery, state: FSMContext):
    if callback_query.data != "toure_place_back":
        data = await state.update_data(counting=callback_query.data)
    else:
        data = await state.get_data()

    await state.set_state(ToureStates.TourePlace)

    # Создаем новую клавиатуру
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(1, get_prev_data(data)), "toure_counting_back"
    )

    # Редактируем текущее сообщение
    await callback_query.message.edit_text(
        "🌍 Отлично! Теперь давайте выберем направление поездки. Куда вы хотите отправиться?",
        reply_markup=keyboard,
    )
    await callback_query.answer("")


# Возвращает пользователя в первый шаг выбора тура
@router.callback_query(ToureStates.TourePlace, F.data == "toure_counting_back")
async def counting_back(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer("Вернёмся обратно!")

    await state.clear()
    await cmd_application(callback_query.message, state)


@router.callback_query(ToureStates.TourePlace)
async def toure_place(callback_query: CallbackQuery, state: FSMContext):
    data = await state.update_data(toure_place=callback_query.data)
    await state.set_state(ToureStates.ToureEnd)

    # Создаем новую клавиатуру
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(2, get_prev_data(data)), "toure_place_back"
    )

    # Редактируем текущее сообщение
    await callback_query.message.edit_text(
        "📅 Здорово! Теперь выберите конкретный тур из доступных вариантов ниже:",
        reply_markup=keyboard,
    )
    await callback_query.answer("")


# Возвращает пользователя во второй шаг выбора тура
@router.callback_query(ToureStates.ToureEnd, F.data == "toure_place_back")
async def toure_place_back(callback_query: CallbackQuery, state: FSMContext):
    await callback_query.answer("Вернёмся обратно!")

    current_data = await state.get_data()
    current_data.pop("toure_place", None)
    await state.set_data(current_data)

    await state.set_state(ToureStates.Counting)

    # Возвращаемся к предыдущему шагу
    await counting(callback_query, state)


@router.callback_query(ToureStates.ToureEnd)
async def get_number(callback_query: CallbackQuery, state: FSMContext):
    await state.update_data(toure_end=callback_query.data)
    keyboard = await create_contact_keyboard()

    # Отправляем новое сообщение с обычной клавиатурой
    await callback_query.message.answer(
        "📱 Отлично! Остался последний шаг — поделитесь своими контактами, чтобы мы могли связаться с вами.",
        reply_markup=keyboard,
    )
    await callback_query.answer("")
    await state.set_state(ToureStates.Contact)


import asyncio
import random


async def show_circular_progress(message: Message):
    # Первое сообщение с шуткой
    first_message = await message.answer(
        "⚙️ Секундочку... Мои шестерёнки уже крутятся в поисках лучшего решения для вас! 🧠",
        reply_markup=ReplyKeyboardRemove(),
    )

    # Второе сообщение — начало загрузки
    loading_message = await message.answer("🚀 Готовлюсь обработать вашу заявку...")
    await asyncio.sleep(1)  # Задержка для имитации работы
    await first_message.delete()  # Удаляем первое сообщение
    await loading_message.edit_text(f"⏳ Обработка заявки... [{'┈' * 10}] 0%")

    await asyncio.sleep(0.5)  # Задержка для имитации работы

    # Анимация кругового прогресса
    for progress in range(10, 101, 10):  # Увеличиваем прогресс на 10% каждый шаг
        bar = "▬" * (progress // 10) + "┈" * (10 - progress // 10)
        await asyncio.sleep(
            random.uniform(0.1, 0.3)
        )  # Случайная задержка для реалистичности
        await loading_message.edit_text(f"⏳ Обработка заявки... [{bar}] {progress}%")

    # Финальное сообщение перед завершением анимации
    await loading_message.edit_text(
        "✨ Делаю последние штрихи... Ваша заявка почти готова!"
    )
    await asyncio.sleep(1)  # Задержка для эффекта
    return loading_message


@router.message(F.content_type == "contact", ToureStates.Contact)
async def toure_end(message: Message, state: FSMContext):
    data = await state.get_data()

    # Показываем анимацию загрузки
    loading_message = await show_circular_progress(message)

    # Имитация обработки данных (например, отправка на сервер)
    await asyncio.sleep(1)

    # Сообщение об успешной обработке
    await message.answer(
        "🎉 Ура! Ваша заявка успешно обработана! ✨\n\n"
        "Если понадобится помощь или захотите узнать больше, просто нажмите /help — я всегда рядом! 😊"
    )
    # Финальное сообщение
    await loading_message.edit_text(
        format_final_message(message, data), parse_mode="HTML"
    )

    await state.clear()
