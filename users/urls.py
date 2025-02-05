from django.urls import path
from .views import (
    RegisterUserView,
    CustomLoginView,
    CustomLogoutView,
    email_verification,
)

app_name = "users"

urlpatterns = [
    path(
        "register/", RegisterUserView.as_view(), name="register"
    ),  # Регистрация пользователя
    path("login/", CustomLoginView.as_view(), name="login"),  # Логин пользователя
    path("logout/", CustomLogoutView.as_view(), name="logout"),  # Выход пользователя
    path(
        "email_confirm/<str:token>", email_verification, name="email-confirm"
    ),  # Верификация почты
]
