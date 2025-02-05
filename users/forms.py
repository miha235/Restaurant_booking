# users/forms.py

from django import forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ["email", "password"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if get_user_model().objects.filter(email=email).exists():
            raise ValidationError("Пользователь с таким email уже существует.")
        return email


class PasswordRecoveryForm(forms.Form):
    email = forms.EmailField()
