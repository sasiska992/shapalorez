from aiogram import F, Router
from aiogram.types import (
    Message,
    KeyboardButton,
    ReplyKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()
print("hello from router")


@router.message(Command("test_1"))
async def cmd_test_1(message: Message):
    kb = [[KeyboardButton(text="С пюрешкой")], [KeyboardButton(text="Без пюрешки")]]
    keyboard = ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)


@router.message(Command("test_2"))
async def cmd_test_2(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text="Тур 1", callback_data="select_toure"))
    builder.add(InlineKeyboardButton(text="Тур 2", callback_data="select_toure"))
    builder.add(InlineKeyboardButton(text="Тур 3", callback_data="select_toure"))
    await message.answer(
        "Выберите тур:",
        reply_markup=builder.as_markup(),
    )


@router.callback_query(F.data == "select_toure")
async def send_random_value(callback: CallbackQuery):
    await callback.message.answer("Тут список доступных туров")
