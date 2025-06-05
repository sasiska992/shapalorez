import os
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton, CallbackQuery
from aiogram.filters.command import Command
from keyboards.create_inline_keyboard import (
    create_inline_keyboard_for_toures_with_button_go_back,
)
from aiogram import F, Router
from aiogram.types import FSInputFile
from aiogram.exceptions import TelegramNetworkError


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
    {"text": "Волчьи ворота", "callback_data": "info_voltchik_vort"},
    {"text": "Десятый километр", "callback_data": "info_desyat_kilometr"},
    {"text": "Кушина", "callback_data": "info_kushina"},
    {"text": "Красный мост", "callback_data": "info_krasnoy_most"},
    {"text": "Отдалённый (Шпалорез)", "callback_data": "info_shapoleroz"},
    {"text": "Матрица", "callback_data": "info_matrya"},
    {"text": "Карта УЖД", "callback_data": "info_karta_uzd"},
]


# Обработчик команды /start
@router.message(Command("infotours"))
async def cmd_infotoures(message: Message):
    image_path = "static/photos/image.png"

    if not os.path.exists(image_path):
        await message.answer("Файл не найден!")
        return

    try:
        photo = FSInputFile(image_path)
        # Здесь написан id фото (Карта УЖД). Если нужно поменять картинку, то выше есть переменная photo, нужно использовать её вместо id
        sent_message = await message.answer_photo(
            # photo=photo,
            photo="AgACAgIAAxkDAAIFAWhBqpokIa0kdyPeqq0wLMHv4nBmAAIo9TEbeeIQSiY78XIZlFBbAQADAgADdwADNgQ",
            caption="Выберите тур из списка ниже",
            reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
                buttons, "back_infotoures"
            ),
        )
        # Нужно, чтобы получить id фото, которое отправлено было. Это нужно для того, чтобы TG захэшировал фото и оно грузилось быстрее
        # file_id = sent_message.photo[-1].file_id
        # await message.answer(f"file_id отправленного фото: {file_id}")
    except TelegramNetworkError as e:
        await message.answer(
            "Ошибка при отправке фото. Возможно, нет интернета или файл слишком большой."
        )
        print(f"TelegramNetworkError: {e}")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
        print(f"Unexpected error: {e}")


@router.callback_query(F.data == "back_infotoures")
async def back_infotoures(callback_query: CallbackQuery):
    await callback_query.answer("")
    await cmd_infotoures(callback_query.message)


@router.callback_query(F.data == "info_voltchik_vort")
async def infotoures_1(callback_query: CallbackQuery):
    await callback_query.message.edit_caption(
        caption="""
🟠 Самый короткий маршрут у нас занимает порядка 2-2,5 часа и называется он «ДоВолчьихВорот!», длина маршрута 16 километров, по пути одна остановка. 
🗺️ Путь следования: станция Черниговская (село Черниговское) - остановка урочище Волчьи ворота - станция Черниговская (село Черниговское). 
🚂 Проводится сборной экскурсией нашим проектом исключительно по расписанию  в 11:00 и в 14:00. 
⚠️ Этот тур самый самый короткий и подойдет для предварительного знакомства с УЖД и нашим проектом. Остановка замет у нас 15-20 минут. Гид в составе группы расскажет-покажет вам все что окружает нас, было в советское время, во времена ВОВ или что там планируется в ближайшее будущее.
    """,
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")


@router.callback_query(F.data == "info_desyat_kilometr")
async def infotoures_2(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """
🟠 Не самый короткий маршрут в нашем арсенале, занимает порядка 3 часов и называется он «ДоДесятого!», длина маршрута 20 километров, по пути одна остановка. 
🗺️ Путь следования: станция Черниговская (село Черниговское) - остановка урочище Волчьи ворота - станция посёлок Десятый километр - станция Черниговская (село Черниговское). Проводится для групп в будние дни, либо сборной экскурсией нашим проектом. 
🚂 Проводится для групп в любые дни, либо сборной экскурсией нашим проектом.
Этот тур самый самый короткий и подойдет для предварительного знакомства с УЖД и нашим проектом. За 3 часа поездки у вас будет две остановки по 15-20 минут каждая. Гид в составе группы на остановках расскажет-покажет вам все что окружает нас, было в советское время, во времена ВОВ или что там планируется в ближайшее будущее.
""",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")


@router.callback_query(F.data == "info_kushina")
async def infotoures_3(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """ 
🟠 Среднеформатный маршрут, занимает порядка 4-5 часов и называется он «НаКушинку!», длина маршрута 25 километров, по пути три остановки.
🗺️ Путь следования: станция Черниговская (село Черниговское) - остановка урочище Волчьи ворота- станция посёлок Десятый километр - станция посёлок Кушинка-станция Черниговская (село Черниговское). 
🚂 Проводится для малых групп в любые дни на дрезине.
⚠️ Этот тур не самый короткий , но в нем много уникальных особенностей: 
 - музей старинной утвари и инструментов
 - старинная водяная мельница, которая сохранилась с начала 19 века. 
За время поездки у вас будет две остановки по 15-20 минут каждая. Гид в составе группы на остановках расскажет-покажет вам все что окружает нас, было в советское время, во времена ВОВ или что там планируется в ближайшее будущее.
""",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")


@router.callback_query(F.data == "info_krasnoy_most")
async def infotoures_4(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """
🟠 Стандартный маршрут у нас занимает порядка 5-6 часов и называется он «ДоКрасного!», длина маршрута 32 километра, по пути шесть остановок. 
🗺️ Путь следования: станция Черниговская (село Черниговское) - остановка Часовня - остановка водопад Паровозный - остановка урочище Волчьи ворота- станция посёлок Десятый километр-станция посёлок Режет - остановка Красный мост (урочище Верхние Волчьи ворота)- станция Черниговская (село Черниговское). 
🚂 Проводится для групп в любые дни, либо сборной экскурсией нашим проектом.
⚠️ Этот тур самый информативный и с самым большим количеством остановок. За 6 часов поездки у вас будет шесть остановок, каждая минут по 15-20. Гид в составе группы на остановках расскажет-покажет вам все что окружает нас, было в советское время, во времена ВОВ или что там планируется в ближайшее будущее.
""",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")


@router.callback_query(F.data == "info_shapoleroz")
async def infotoures_5(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """
🟠 Полный маршрут у нас занимает порядка 6 часов и называется он «НаШпалорез!», длина маршрута 64 километра, по пути две остановки. 
🗺️ Путь следования: станция Черниговская (село Черниговское) - остановка урочище Волчьи ворота - остановка Красный мост (урочище Верхние Волчьи ворота) - остановка посёлок Средние Тубы - станция Шпалорез (посёлок Отдалённый) - станция Черниговская (село Черниговское). 
🚂 Проводится для малых групп в любые дни на дрезине.
⚠️ Этот тур подходит для истинных фанатов и энтузиастов узкоколеек, для тех кто хочет проехать Апшеронскую УЖД от первой и до последней шпалы и увидеть все ее красоты непосредственно из вагона нашего состава.
""",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")


@router.callback_query(F.data == "info_matrya")
async def infotoures_6(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """
🟠 Будние поездки у нас занимают порядка 3 часа и называются «Легендарная Матрица!», длина маршрута 30 километров, по пути нет остановок и в составе нет гида.
🗺️ Путь следования: станция Черниговская (село Черниговское) - станция посёлок Десятый километр-станция посёлок Режет - станция Черниговская (село Черниговское). 
🚂 Проводится будние дни, по понедельникам средам и пятницам в 6:00 и 15:10.
""",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")


@router.callback_query(F.data == "info_karta_uzd")
async def infotoures_7(callback_query: CallbackQuery):
    await callback_query.message.answer(
        """
Пока не готово
""",
        reply_markup=await create_inline_keyboard_for_toures_with_button_go_back(
            buttons, "back_infotoures"
        ),
    )
    await callback_query.answer("")
