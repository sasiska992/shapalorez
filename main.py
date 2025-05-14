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
)

logging.basicConfig(level=logging.INFO)

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


async def set_commands():
    commands = [
        BotCommand(command="start", description="Старт"),
        BotCommand(command="help", description="help"),
        BotCommand(command="info", description="Информация"),
        BotCommand(command="application", description="Оставить заявку"),
    ]
    await bot.set_my_commands(commands, BotCommandScopeDefault())


async def main():
    dp.include_router(start_router)
    dp.include_router(help_router)
    dp.include_router(toure_router)
    dp.include_router(info_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_commands()


if __name__ == "__main__":
    asyncio.run(main())
