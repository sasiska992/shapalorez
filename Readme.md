# 🌟 Shpalorez Tour Booking Bot

[![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)](https://www.python.org/) 
[![Aiogram](https://img.shields.io/badge/Aiogram-3.x-green?logo=telegram)](https://docs.aiogram.dev/en/latest/)
[![Docker](https://img.shields.io/badge/Docker-blue?logo=docker)](https://www.docker.com/)

Этот Telegram-бот помогает пользователям легко забронировать тур через компанию [Shpalorez](https://shpalorez.com). Бот создан с использованием современных технологий, таких как **Python**, **Aiogram 3.x**, и **Docker**.

---

## 📸 Скриншоты бота

Здесь вы можете увидеть, как выглядит бот в действии:

![Screenshot 1](https://via.placeholder.com/600x400?text=Screenshot+1)  
*Главное меню бота*

![Screenshot 2](https://via.placeholder.com/600x400?text=Screenshot+2)  
*Процесс бронирования тура*


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
- `/info` — Узнать больше о компании и контактах.
- `/application` — Оставить заявку на бронирование тура.

---

## 🚀 Как запустить проект

### 1. Клонируйте репозиторий
```bash
git clone https://github.com/sasiska992/shapalorez
cd shpalorez-bot
```

### 2. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта и добавьте переменные окружения `понадобится лишь BOT_TOKEN`: 
```env
BOT_TOKEN=your_telegram_bot_token_here
```

### 3. Добавьте файл со струтурой туров.
Вам нужно добавить файл со структурой туров в директорию **utils/toures.json**.

Файл **utils/toures_demo.json** содержит структуру данных для туров. Вам останется лишь добавить туры в этот файл.

### 4. Запуск через Docker
Убедитесь, что у вас установлены **Docker** и **Docker Compose**.

#### a) Создайте образ Docker
```bash
docker build -t shpalorez .
```

#### b) Запустите контейнер
```bash
docker run -d shpalorez:latest
```

Теперь ваш бот запущен и готов к работе!

---

## 🌐 Ссылки

- [Telegram API](https://core.telegram.org/bots/api)
- [Aiogram Documentation](https://docs.aiogram.dev/en/latest/)
- [Docker Documentation](https://docs.docker.com/)
