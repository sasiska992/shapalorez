from aiogram.types import Message
from handlers.toures.toure import get_prev_data
from utils.toures import get_labels_by_callback_path
from .toures import get_prev_data


def format_final_message(message: Message, data: list[str]):
    """
    Формирует красивое и информативное сообщение на основе данных пользователя и выбранного тура.

    Args:
        message (aiogram.types.Message): Объект сообщения от Telegram-бота.
        data (list): Список callback_data, представляющий путь по структуре тура,
                     например: ['more_6', 'full_mangal', 'kushina']

    Returns:
        str: HTML-форматированное сообщение для отправки администратору или логирования.
    """
    # Получаем текстовые метки из callback-пути
    prev_data = get_prev_data(data)
    result = get_labels_by_callback_path(prev_data)

    # Извлекаем имя пользователя
    name = ""
    if message.contact:
        if message.contact.first_name:
            name += message.contact.first_name
        if message.contact.last_name:
            name += " " + message.contact.last_name

    # Получаем имя пользователя в Telegram
    tg_username = message.from_user.username
    username_link = f"@{tg_username}" if tg_username else "(нет)"

    username = message.from_user.username
    username_link = f"@{username}" if username else "<b> Нет </b>"
    phone_number = message.contact.phone_number if message.contact else "<b> Не предоставлен </b>"
    name = message.contact.first_name if message.contact else "<b> Не указано </b>"

    # Формируем красивое сообщение
    formatted_message = (
        f"<b>📬 Новый запрос на бронирование тура</b>\n\n"
        f"<b>👥 Количество человек:</b> {result[0]}\n\n"
        f"<b>🎫 Выбранный тур:</b> {result[1]}\n\n"
        f"<b>📍 Место назначения:</b> {result[2]}\n\n"
        f"<b>👤 Имя клиента:</b> {name}\n\n"
        f"<b>📞 Контактный телефон:</b> {phone_number}\n\n"
        f"<b>📱 Telegram:</b> {username_link}"
    )

    return formatted_message
