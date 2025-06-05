from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command
from aiogram import F

from aiogram import Router

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    help_text = """

🚀 Доступные команды:

/start - Запуск 🚂

/zakaz - Оставить заявку 🚂🎫

/infoturs - О всех наших турах 🗺️

/contacts - Наши контакты ☎️

/help - Помощь по командам🚨
"""
    await message.answer(help_text, parse_mode="HTML")


@router.message(F.data == "back_help")
async def back_help(message: Message):
    await message.answer("Вернуться назад")
    await cmd_help(message)
