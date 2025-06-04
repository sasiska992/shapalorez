from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def create_inline_keyboard_for_toures_with_button_go_back(
    data: list[dict], callback_data_to_back: str
) -> InlineKeyboardMarkup:
    """Создает inline-клавиатуру для выбора тура с кнопкой "Назад".


    Args:
        data (list[dict]): Данные, которые нужно отобразить в клавиатуре.
        callback_data_to_back (str): callback_data для кнопки "Назад".

    Returns:
        InlineKeyboardMarkup: Клавиатура с кнопкой "Назад".
    """
    builder = InlineKeyboardBuilder()
    for item in data:
        builder.button(
            text=item["text"],
            callback_data=item["callback_data"],
        )
    builder.button(text="Назад", callback_data=callback_data_to_back)
    builder.adjust(1)  # Каждая кнопка на новой строке
    return builder.as_markup()
