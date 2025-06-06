from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery
from aiogram.filters.command import Command
from keyboards.send_number import create_contact_keyboard
from keyboards.create_inline_keyboard import (
    create_inline_keyboard_for_toures_with_button_go_back,
)
from states.toures import ToureStates
from utils.tours import get_next_values, get_prev_data
from utils.format_final_message import format_final_message
import random

import asyncio


from aiogram.types import ReplyKeyboardRemove

from handlers.help import cmd_help

router = Router()


@router.message(Command("zakaz"))
async def cmd_application(message: Message, state: FSMContext) -> None:
    """
    Обработчик команды application.

    Args:
        message (aiogram.types.Message): Сообщение, которое приходит от пользователя.
        state (aiogram.fsm.context.FSMContext): Текущее состояние

    Returns:
        None
    """
    await state.clear()
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(0, []), "toures_application_help"
    )
    await state.set_state(ToureStates.Counting)
    await message.answer(
        "👋 Привет! Сколько человек планируют участвовать в туре? Выберите вариант ниже:",
        reply_markup=keyboard,
    )


@router.callback_query(ToureStates.Counting, F.data == "toures_application_help")
async def application_help(callback_query: CallbackQuery, state: FSMContext):
    """
    Возвращает пользователя в случае необходимости в команду /help
    Очищается состояние, то есть логика начинается заново

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    await callback_query.answer("")
    await state.clear()

    await cmd_help(callback_query.message)


@router.callback_query(ToureStates.Counting)
async def counting(callback_query: CallbackQuery, state: FSMContext):
    """Первый шаг выбора тура (выбирается количество человек)

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    if callback_query.data != "toure_place_back":
        # Если попали сюда из кнопки "Назад" на следующем шаге.
        # Если этого условия нет, то в состояние будет записываться ненужная информация
        data = await state.update_data(counting=callback_query.data)
    else:
        data = await state.get_data()

    await state.set_state(ToureStates.TourePlace)

    # Создаем новую клавиатуру на основе прошлого шага
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        get_next_values(1, get_prev_data(data)), "toure_counting_back"
    )

    # Редактируем текущее сообщение
    await callback_query.message.edit_text(
        "🌍 Отлично! Теперь давайте выберем направление поездки. Куда вы хотите отправиться?",
        reply_markup=keyboard,
    )
    await callback_query.answer("")


@router.callback_query(ToureStates.TourePlace, F.data == "toure_counting_back")
async def counting_back(callback_query: CallbackQuery, state: FSMContext):
    """
    Возвращает пользователя в первый шаг выбора тура. То есть вызывается функция cmd_application

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    await callback_query.answer("Вернёмся обратно!")

    await state.clear()
    await cmd_application(callback_query.message, state)


@router.callback_query(ToureStates.TourePlace)
async def toure_place(callback_query: CallbackQuery, state: FSMContext):
    """
    Выбирается второй шаг выбора тура

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """

    if callback_query.data == "toure_time_back":
        # Если попали сюда из кнопки "Назад" на следующем шаге.
        # Если этого условия нет, то в состояние будет записываться ненужная информация
        data = await state.get_data()
    else:
        data = await state.update_data(toure_place=callback_query.data)
    next_info = get_next_values(2, get_prev_data(data))
    if {"text": "Понедельник", "callback_data": "ponedelnik"} in next_info:
        # Переход в другую ветку. А именно с выбором даты
        await state.set_state(ToureStates.ToureDate)
    else:
        await state.set_state(ToureStates.ToureEnd)
    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        next_info, "toure_place_back"
    )

    # Редактируем текущее сообщение
    await callback_query.message.edit_text(
        "📅 Здорово! Теперь выберите конкретный тур из доступных вариантов ниже:",
        reply_markup=keyboard,
    )
    await callback_query.answer("")


@router.callback_query(ToureStates.ToureEnd, F.data == "toure_place_back")
async def toure_place_back(callback_query: CallbackQuery, state: FSMContext):
    """
    Возвращает пользователя во второй шаг выбора тура

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    await callback_query.answer("Вернёмся обратно!")

    # Убираем toure_place из данных в состоянии
    current_data = await state.get_data()
    current_data.pop("toure_place", None)

    # Обновляем данные в состоянии
    await state.set_data(current_data)

    await state.set_state(ToureStates.Counting)

    # Возвращаемся к предыдущему шагу
    await counting(callback_query, state)


@router.callback_query(ToureStates.ToureDate, F.data == "toure_place_back")
async def toure_place_back(callback_query: CallbackQuery, state: FSMContext):
    """
    Возвращает пользователя во второй шаг выбора тура

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    await callback_query.answer("Вернёмся обратно!")

    # Убираем toure_place из данных в состоянии
    current_data = await state.get_data()
    current_data.pop("toure_place", None)

    # Обновляем данные в состоянии
    await state.set_data(current_data)

    await state.set_state(ToureStates.Counting)

    # Возвращаемся к предыдущему шагу
    await counting(callback_query, state)


@router.callback_query(ToureStates.ToureDate)
async def toure_date(callback_query: CallbackQuery, state: FSMContext):
    """
    Возвращает пользователя в третий шаг выбора тура

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    data = await state.update_data(toure_date=callback_query.data)
    next_info = get_next_values(3, get_prev_data(data))

    keyboard = await create_inline_keyboard_for_toures_with_button_go_back(
        next_info, "toure_time_back"
    )

    # Редактируем текущее сообщение
    await callback_query.message.edit_text(
        "⏰ Супер! Теперь выбираем время поездки 👇🏼",
        reply_markup=keyboard,
    )
    await callback_query.answer("")
    await state.set_state(ToureStates.ToureEnd)


@router.callback_query(ToureStates.ToureEnd, F.data == "toure_time_back")
async def toure_time_back(callback_query: CallbackQuery, state: FSMContext):
    """Возвращает пользователя во второй шаг выбора тура

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    await callback_query.answer("Вернёмся обратно!")

    # Убираем toure_date из данных в состоянии
    current_data = await state.get_data()
    current_data.pop("toure_date", None)
    # Обновляем данные в состоянии
    await state.set_data(current_data)

    await state.set_state(ToureStates.TourePlace)

    # Возвращаемся к предыдущему шагу
    await toure_place(callback_query, state)


@router.callback_query(ToureStates.ToureEnd)
async def get_number(callback_query: CallbackQuery, state: FSMContext):
    """
    Возвращает пользователя в последний шаг выбора тура, где нужно оставить контактные данные

    Args:
        callback_query (CallbackQuery): Нажатие кнопки пользователем
        state (FSMContext): Текущее состояние
    """
    await state.update_data(toure_end=callback_query.data)
    keyboard = await create_contact_keyboard()

    # Отправляем новое сообщение с обычной клавиатурой
    await callback_query.message.answer(
        "📱 Отлично! Остался последний шаг — поделитесь своими контактами, чтобы мы могли связаться с вами.\n"
        "Для этого достаточно нажать на кнопку, которая появилась под вводом сообщения",
        reply_markup=keyboard,
    )
    await callback_query.answer("")
    await state.set_state(ToureStates.Contact)


async def show_circular_progress(message: Message) -> Message:
    """Создает анимацию загрузки и возвращает её сообщение.

    Args:
        message (Message): Сообщение, на которое нужно отобразить анимацию.

    Returns:
        Message: Сообщение, в котором содержится загрузка.
    """
    # first_message = await message.answer(
    #     "⚙️ Секундочку... Мои шестерёнки уже крутятся в поисках лучшего решения для вас! 🧠",
    #     reply_markup=ReplyKeyboardRemove(),
    # )

    # Второе сообщение — начало загрузки
    loading_message = await message.answer("🚀 Готовлюсь обработать вашу заявку...")
    await asyncio.sleep(1)  # Задержка для имитации работы
    # await first_message.delete()  # Удаляем первое сообщение
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
    """Финальная функция для обработки заявки на тур.

    Args:
        message (Message): Полученное сообщение от пользователя.
        state (FSMContext): Текущее состояние.
    """
    data = await state.get_data()

    # Показываем анимацию загрузки
    loading_message = await show_circular_progress(message)

    # Имитация обработки данных (например, отправка на сервер)
    await asyncio.sleep(1)

    # Сообщение об успешной обработке
    await message.answer(
        """
🚂🎉 Ваша заявка сформирована! в скором времени вам ответят🤝🏼

Если понадобится помощь - жмём /help — я тут! 😊
        """,
    )
    # финальное сообщение
    await loading_message.edit_text(
        format_final_message(message, data), parse_mode="HTML"
    )

    await state.clear()
