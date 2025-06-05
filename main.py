import asyncio
from aiogram import Bot, Dispatcher

from aiogram.types import (
    BotCommand,
    BotCommandScopeDefault,
)
import logging

from config import BOT_TOKEN

from handlers import (
    start_router,
    help_router,
    toure_router,
    info_router,
    contacts_router
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def set_commands():
    commands = [
        BotCommand(command="start", description="Запуск 🚂"),
        BotCommand(command="help", description="Помощь по командам🚨"),
        BotCommand(command="infotoures", description="О всех наших турах 🗺️"),
        BotCommand(command="contacts", description="Наши контакты ☎️"),
        BotCommand(command="application", description="Оставить заявку"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(toure_router)
    dp.include_router(info_router)
    dp.include_router(contacts_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_commands()


if __name__ == "__main__":
    asyncio.run(main())
