from aiogram.types import Message, CallbackQuery
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

/infotours - О всех наших турах 🗺️

/contacts - Наши контакты ☎️

/help - Помощь по командам🚨
"""
    await message.answer(help_text, parse_mode="HTML")


@router.callback_query(F.data == "back_help")
async def back_help(callback_query: CallbackQuery):
    await callback_query.answer("")
    await cmd_help(callback_query.message)

# @router.message(Command("id"))
# async def cmd_id(message: Message):
#     await message.answer("Ваш id пользователя: `{}`".format(message.from_user.id), parse_mode="Markdown")