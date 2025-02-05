from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView
from django.core.mail import send_mail
from django.conf import settings
from .forms import RegistrationForm, PasswordRecoveryForm

import random
import string
import secrets

from .models import User


class RegisterUserView(FormView):
    template_name = 'users/registration/register.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('users:login')  # Перенаправление на страницу входа после успешной регистрации

    def form_valid(self, form):
        # Сохранение пользователя
        user = form.save(commit=False)
        #user.username = user.email.split('@')[0]
        user.is_active = False
        user.set_password(form.cleaned_data['password'])
        # Генерация кода подтверждения
        token = secrets.token_hex(16) # verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email_confirm/{token}'

        # Отправка письма с кодом
        try:
            send_mail(
                'Подтверждение почты',
                f'Перейдите по ссылке для подтверждения почты: {url}',
                settings.EMAIL_HOST_USER,  # Email отправителя из settings.py
                [user.email],  # Email получателя
                fail_silently=False,
            )
            print()
        except Exception as e:
            # Логирование или обработка ошибки
            print(f"Ошибка при отправке письма: {e}")

        return super().form_valid(form)


class CustomLoginView(LoginView):
    template_name = 'users/registration/login.html'  # Укажите путь к вашему шаблону
    redirect_authenticated_user = False  # Отключить перенаправление
    success_url = reverse_lazy('index')  # Укажите вашу домашнюю страницу

    def get_success_url(self):
        """Переопределите метод, чтобы перенаправить пользователя после успешного входа."""
        return self.success_url

class CustomLogoutView(LogoutView):
    success_url = reverse_lazy('index')

    def get_success_url(self):
        """Переопределите метод, чтобы перенаправить пользователя после успешного входа."""
        return self.success_url

class PasswordRecoveryView(FormView):
    template_name = 'users/registration/recover_password.html'
    form_class = PasswordRecoveryForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        try:
            user = get_user_model().objects.get(email = email)
        except get_user_model().DoesNotExist:
            return redirect('password_recovery_failed')

        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k = 8))
        user.set_password(new_password)
        user.save()

        send_mail(
            'Восстановление пароля',
            f'Ваш новый пароль: {new_password}',
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently = False,
        )
        return super().form_valid(form)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    print(user)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))
