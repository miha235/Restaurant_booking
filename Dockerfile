# Используем официальный образ Python как базовый
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt /app/

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект в рабочую директорию контейнера
COPY . /app/

# Устанавливаем переменную окружения для того, чтобы Python не записывал .pyc файлы
ENV PYTHONDONTWRITEBYTECODE 1

# Устанавливаем переменную окружения для оптимизации вывода Python
ENV PYTHONUNBUFFERED 1

# Открываем порт для работы приложения (по умолчанию Django использует 8000)
EXPOSE 8000

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
