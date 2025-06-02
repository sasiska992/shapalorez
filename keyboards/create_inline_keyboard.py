from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_inline_keyboard_for_toures_with_button_go_back(
    data: list[dict], callback_data_to_back: str
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in data:
        builder.button(
            text=item["text"],
            callback_data=item["callback_data"],
        )
    builder.button(text="Назад", callback_data=callback_data_to_back)
    builder.adjust(1)  # Каждая кнопка на новой строке
    return builder.as_markup()
