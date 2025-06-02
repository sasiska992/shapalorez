from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command


from aiogram import Router

router = Router()


@router.message(Command("info"))
async def cmd_start(message: Message):
    message_text = (
        "🌟 **Информация о нас:**\n\n"
        "Мы — команда профессионалов, которые помогают организовать незабываемые путешествия! 🚀\n\n"
        "🌐 **Наш сайт:** [shpalorez.com](https://shpalorez.com)\n"
        "💼 **Vk:** [vk.com/shpalorezuzd](https://vk.com/shpalorezuzd)\n"
        "✉️ **Telegram:** [t.me/shpalorez](https://t.me/shpalorez)\n"
        "📱 **WhatsApp:** [wa.me/message/VZA2AYXNFPUAN1](https://wa.me/message/VZA2AYXNFPUAN1)\n"
        "📸 **Instagram:** [instagram.com/shpalorez](https://www.instagram.com/shpalorez)\n"
        "🎥 **YouTube:** [youtube.com/c/ShpalorezExpress](https://www.youtube.com/c/ShpalorezExpress)\n"
        "👥 **OK:** [ok.ru/group/70000001221997](https://ok.ru/group/70000001221997)\n"
        "👍 **Facebook:** [facebook.com/shpalorezuzd](https://www.facebook.com/shpalorezuzd)\n\n"
        "☎️ **Телефоны для связи:**\n"
        "+7 (861) 205-55-05\n"
        "+7 (989) 199-86-86"
    )
    await message.answer(message_text, parse_mode="Markdown")
