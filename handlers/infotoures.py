from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.filters.command import Command
from keyboards.create_inline_keyboard import (
    create_inline_keyboard_for_toures_with_button_go_back,
)
from aiogram import F, Router

router = Router()


# @router.message(Command("infotoures"))
# async def cmd_infotoures(message: Message):
#     await message.answer_photo(
#         caption="""🟠 Будние поездки у нас занимают порядка 3 часа и называются «Легендарная Матрица!», длина маршрута 30 километров, по пути нет остановок и в составе нет гида.
# 🗺️ Путь следования: станция Черниговская (село Черниговское) - станция посёлок Десятый километр-станция посёлок Режет - станция Черниговская (село Черниговское).
# 🚂 Проводится будние дни, по понедельникам средам и пятницам в 6:00 и 15:10.
# """,
#         photo="https://cdn-ru.bitrix24.ru/b23889936/landing/bbf/bbfee6deb47f61bd5ea2af45db870333/IMG_6736_1x.jpeg",
#         parse_mode="Markdown",
#     )
# await message.answer(
#     text="""🟠 Будние поездки у нас занимают порядка 3 часа и называются «Легендарная Матрица!», длина маршрута 30 километров, по пути нет остановок и в составе нет гида.
# 🗺️ Путь следования: станция Черниговская (село Черниговское) - станция посёлок Десятый километр-станция посёлок Режет - станция Черниговская (село Черниговское).
# 🚂 Проводится будние дни, по понедельникам средам и пятницам в 6:00 и 15:10.""",
#     parse_mode="Markdown"
# )

# await message.answer_photo(
#     photo="https://cdn-ru.bitrix24.ru/b23889936/landing/bbf/bbfee6deb47f61bd5ea2af45db870333/IMG_6736_1x.jpeg"
# )
# await message.answer("Давайте я вам подробно расскажу про туры", parse_mode="Markdown")

# Список кнопок
buttons = [
    {"text": "Волчьи ворота", "callback_data": "1"},
    {"text": "Легендарная матрица", "callback_data": "2"},
    {"text": "Поездка по Черниговской", "callback_data": "3"},
    {"text": "Поездка по Режету", "callback_data": "4"},
    {"text": "Поездка по Десятому километру", "callback_data": "5"},
    {"text": "Кушинка", "callback_data": "6"},
    {"text": "Красный мост", "callback_data": "7"},
    {"text": "Отдаленный (Шпалорез)", "callback_data": "8"},
    {"text": "Матрица", "callback_data": "9"},
    {"text": "Карта УЖД", "callback_data": "10"},
]


# Обработчик команды /start
@router.message(Command("infotoures"))
async def cmd_infotoures(message: Message):
    await message.answer(
        "Выберите тур из списка ниже",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "infotoures"
        ),
    )


@router.callback_query(F.data == "1")
async def cmd_infotoures_1(callback_query: CallbackQuery):
    await callback_query.message.answer_photo(
        caption="""🟠 Будние поездки у нас занимают порядка 3 часа и называются «Легендарная Матрица!», длина маршрута 30 километров, по пути нет остановок и в составе нет гида.
🗺️ Путь следования: станция Черниговская (село Черниговское) - станция посёлок Десятый километр-станция посёлок Режет - станция Черниговская (село Черниговское).
🚂 Проводится будние дни, по понедельникам средам и пятницам в 6:00 и 15:10.
""",
        photo="https://cdn-ru.bitrix24.ru/b23889936/landing/bbf/bbfee6deb47f61bd5ea2af45db870333/IMG_6736_1x.jpeg",
        parse_mode="Markdown",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "infotoures"
        ),
    )
    await callback_query.answer("")
