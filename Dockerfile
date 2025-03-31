# Используйте официальный образ Python как базовый
FROM python:3.12-slim

# Установите зависимости
RUN apt-get update && apt-get install -y \
    gcc \
    libc-dev \
    && rm -rf /var/lib/apt/lists/*

# Скопируйте текущие файлы в контейнер
WORKDIR /app
COPY requirements.txt .

# Установите Python-зависимости
RUN pip install -r requirements.txt

# Скопируйте остальные файлы проекта
COPY . .

# Откройте порт 8000 для приложения
EXPOSE 8000

# Запустите сервер при запуске контейнера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
