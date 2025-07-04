# 🌟 Shpalorez Tour Booking Bot

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/) 
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green?logo=telegram)](https://docs.aiogram.dev/en/latest/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker)](https://www.docker.com/)

Этот Telegram-бот помогает пользователям легко забронировать тур через компанию [Shpalorez](https://shpalorez.com). Бот создан с использованием современных технологий, таких как **Python**, **Aiogram 3.x**, и **Docker**.

---

## 🤖 Работающий бот

Здесь вы можете увидеть, как выглядит бот в действии -> [https://t.me/shpalorez_bot](https://t.me/shpalorez_bot)

---

## 🛠 Технологический стек

Для разработки этого проекта использовались следующие технологии:

### Языки программирования:
- **Python** — основной язык для разработки бэкенда.

### Фреймворки и библиотеки:
- **Aiogram 3.x** — для создания Telegram-бота.
- **Asyncio** — для асинхронного выполнения задач.

### Инструменты развертывания:
- **Docker** — для контейнеризации приложения.

### Дополнительные инструменты:
- **Git** — для контроля версий.

---

## 📚 Команды бота

Вот список доступных команд:

- `/start` — Запустить бота и начать работу.
- `/help` — Получить помощь по командам.
- `/contacts` — Узнать больше о компании и контактах.
- `/infotours` — Узнать больше о турах.
- `/zakaz` — Оставить заявку на бронирование тура.

---

## 🚀 Как запустить проект

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/sasiska992/shapalorez
cd shpalorez
```

### 2. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта и добавьте переменнфые окружения `BOT_TOKEN` и `ADMINS` - Telegram-ID администраторов бота.
```env
BOT_TOKEN=your_telegram_bot_token_here
ADMINS=your_telegram_admin_ids_here # example: 123456789,987654321
```

### 3. Запуск без Docker `через python3`
Убедитесь, что у вас установлен **Python 3.x** и **pip**.

```bash
python -V
pip -V
```

#### a) Установите зависимости
```bash
pip install -r requirements.txt
```

#### b) Запустите бота
```bash
python3 main.py  
```

### 4. Запуск через Docker
Убедитесь, что у вас установлен **Docker**.

```bash
docker -v
```

#### a) Создайте образ Docker
```bash
docker build -t shpalorez-bot .
```

#### b) Запустите контейнер
```bash
docker run --name shpalorez_tg_bot -d shpalorez-bot
```

Теперь ваш бот запущен и готов к работе!

---

## 🌐 Ссылки

- [Telegram API](https://core.telegram.org/bots/api)
- [Aiogram Documentation](https://docs.aiogram.dev/en/latest/)
- [Docker Documentation](https://docs.docker.com/)
