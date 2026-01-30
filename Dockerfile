# Используем базовый образ с Python
FROM python:3.12-slim

# Указываем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем requirements.txt для установки зависимостей
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходный код приложения
COPY . .

# Команда для запуска приложения
CMD ["python3", "main.py"]