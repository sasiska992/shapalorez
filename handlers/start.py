from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command


from aiogram import Router

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    welcome_message = (
        "🌟 **Добро пожаловать в онлайн-помощника Shpalorez!** 🌟\n\n"
        "Я здесь, чтобы помочь вам организовать незабываемое путешествие! 🚂\n\n"
        "📍 Выберите направление, узнайте о доступных турах или оставьте заявку — я всегда готов помочь! 😊\n\n"
        "Если понадобится помощь, просто нажмите /help — я расскажу, как со мной взаимодействовать. 📚"
    )

    await message.answer(welcome_message, parse_mode="Markdown")
