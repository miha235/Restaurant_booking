from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('about/', views.about, name='about'),  # О ресторане
    path('reservations/', views.reservation, name='reservation'),  # Бронирование
    path('profile/', views.profile, name='profile'),  # Личный кабинет
    path('reservations/book/', views.book, name='book'), # Для обработки POST-запроса на бронирование
    path('contact/', views.contact, name='contact'),  # Обратная Связь
]
