from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_inline_keyboard(data: list[dict]) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in data:
        builder.button(
            text=item["text"],
            callback_data=item["callback_data"],
        )
    builder.adjust(1)  # Каждая кнопка на новой строке
    return builder.as_markup()
