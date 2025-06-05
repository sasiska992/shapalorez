from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command
from aiogram import F

from aiogram import Router

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = (
        "🚀 <b>Список доступных команд:</b>\n\n"
        "/start - Запустить бота и начать работу 🎯\n"
        "/help - Получить помощь по командам ℹ️\n"
        "/info - Узнать больше о нас и наших контактах 🌐\n"
        "/application - Оставить заявку на участие в туре 🚂"
    )
    await message.answer(help_text, parse_mode="HTML")


@router.message(F.data == "back_help")
async def back_help(message: Message):
    await message.answer("Вернуться назад")
    await cmd_help(message)
