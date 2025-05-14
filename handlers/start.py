from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command


from aiogram import Router

router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer("Добро пожаловать в онлайн-помощника Shpalorez!")
