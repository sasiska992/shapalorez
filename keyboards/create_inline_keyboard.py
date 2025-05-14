from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


# async def create_inline_keyboard(data: list[dict]) -> InlineKeyboardMarkup:
#     print(data)
#     builder = InlineKeyboardBuilder()
#     for item in data:
#         builder.row(
#             InlineKeyboardButton(
#                 text=item["text"],
#                 callback_data=item["callback_data"],
#             )
#         )
#     return builder.as_markup()


async def create_inline_keyboard(data: list[dict]) -> InlineKeyboardBuilder:
    print(data)
    builder = InlineKeyboardBuilder()
    for item in data:
        builder.button(
            text=item["text"],
            callback_data=item["callback_data"],
            # callback_data="aobab",
        )
    return builder
