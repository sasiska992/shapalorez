from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command

from aiogram import Router

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("Команды, которые могут вам помочь:\n" \
    "/info - информация ...")
