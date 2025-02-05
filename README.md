# Restaurant Booking System

Это проект для системы бронирования ресторанов. Он включает в себя регистрацию пользователей, аутентификацию и другие функции, такие как подтверждение email, восстановление пароля и возможность входа в систему.

## Установка

1. Клонируйте репозиторий на свою машину:

    ```bash
    git clone <URL-репозитория>
    ```

2. Перейдите в директорию проекта:

    ```bash
    cd restaurant_booking
    ```

3. Установите виртуальное окружение:

    ```bash
    python -m venv venv
    ```

4. Активируйте виртуальное окружение:

    - Для macOS/Linux:
      ```bash
      source venv/bin/activate
      ```
    - Для Windows:
      ```bash
      venv\Scripts\activate
      ```

5. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

6. Примените миграции базы данных:

    ```bash
    python manage.py migrate
    ```

7. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

8. Откройте браузер и перейдите по адресу:

    ```
    http://127.0.0.1:8000
    ```

## Функционал

- **Регистрация**: Пользователи могут зарегистрироваться с подтверждением email.
- **Вход**: Зарегистрированные пользователи могут входить в систему.
- **Восстановление пароля**: Возможность сбросить забытый пароль.
- **Подтверждение email**: Пользователь получает письмо с подтверждением на указанный email после регистрации.

## Технологии

- Django 4.x
- Python 3.x
- SQLite (по умолчанию)

## Настройки

1. Для отправки писем в Django настройте параметры в `settings.py`:

    ```python
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'  # Пример для Gmail
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'your-email@example.com'
    EMAIL_HOST_PASSWORD = 'your-email-password'
    ```

2. Убедитесь, что ваш SMTP-сервер настроен и работает правильно для отправки email-сообщений.

## Лицензия

Этот проект доступен под лицензией MIT.
