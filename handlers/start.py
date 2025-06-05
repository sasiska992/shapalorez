from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command


from aiogram import Router

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_message = """
🚂 Добро пожаловать на Апшеронскую узкоколейку! Единственную горную УЖД в России! 🇷🇺

🙋🏻‍♂️Я виртуальный ассистент проекта @shpalorez, я помогу Вам выбрать! 🚂

➡️ Выбираем на чем едем, день, длительность, доступные туры и оставляем заявку — я в этом помогу! 😊

⚠️ Если понадобится помощь, просто жми /help — я расскажу, как со мной работать. 📚
"""

    await message.answer(welcome_message, parse_mode="Markdown")
