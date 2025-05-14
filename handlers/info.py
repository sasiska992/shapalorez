from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command


from aiogram import Router

router = Router()


@router.message(Command("info"))
async def cmd_start(message: Message):
    await message.answer(
        """
Наши сообщества в социальных сетях:
Shpalorez-Express:

➤ Our web: https://shpalorez.com

➤ Vkontakte:   https://vk.com/shpalorezuzd
➤Telegram: https://t.me/shpalorez
➤WhatsApp: https://wa.me/message/VZA2AYXNFPUAN1
➤ Insta:   https://www.instagram.com/shpalorez
➤ YouTube:   https://www.youtube.com/c/ShpalorezExpress
➤ OK: https://ok.ru/group/70000001221997
➤ Fb:   https://www.facebook.com/shpalorezuzd
☎ Tel: +7 (861) 205-55-05 
☎ Tel: +7 (989) 199-86-86"""
    )
