from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
)
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_contact_keyboard() -> ReplyKeyboardMarkup:
    """Создает клавиатуру для отправки контакта.

    Returns:
        ReplyKeyboardMarkup: Клавиатура для отправки контакта.
    """
    kb_list = [
        [KeyboardButton(text="Поделиться номером", request_contact=True)],
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb_list,
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Отправьте контакты для связи:",
    )
    return keyboard
