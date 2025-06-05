from aiogram.types import (
    Message,
)
from aiogram.filters.command import Command


from aiogram import Router

router = Router()


@router.message(Command("contacts"))
async def cmd_start(message: Message):
    message_text = """
**📳 Наши контакты**

👨🏻‍💻 [Наш сайт](https://shpalorez.com/) 
📆 [Расписание экскурсий](https://shpalorez.com/raspisanie/) 
🔵 [Vkontakte](https://vk.com/shpalorezuzd) 
⚫️ [Telegram](https://t.me/shpalorez) 
🟣 [Instagram](https://www.instagram.com/shpalorez) 
🔴 [YouTube](https://www.youtube.com/c/ShpalorezExpress) 
🟠 [Одноклассники](https://ok.ru/group/70000001221997) 
🔵 [Facebook](https://www.facebook.com/shpalorezuzd) 

🟢 [WhatsApp (Общий)](https://wa.me/message/VZA2AYXNFPUAN1) 
🟢 [WhatsApp (Расписание)](https://chat.whatsapp.com/IF6lI9ekz1DBp99IUbOYVR) 
🗺️ [Локация станции отправления](https://yandex.ru/maps/-/CCUS4QaZLB) 
☎️ +7 (861) 205-55-05 
📱 +7 (989) 199-86-86
   """
    await message.answer(message_text, parse_mode="Markdown")
