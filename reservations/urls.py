from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('about/', views.about, name='about'),  # О ресторане
    path('reservations/', views.Reservation_Create.as_view(), name='reservation_create'),  # Бронирование reservation_create
    path('profile/', views.profile, name='profile'),  # Личный кабинет
    #path('reservations/<int:id>/reservation_view', views.reservation_view, name='reservation_view'),  # Удалить бронирование
    path('reservations/<int:pk>/reservation_update', views.Reservation_Update.as_view(), name='reservation_update'),  # Редактировать бронирование
    path('reservations/<int:id>/reservation_delete', views.reservation_delete, name='reservation_delete'),  # Удалить бронирование
    path('reservations/book/', views.book, name='book'), # Для обработки POST-запроса на бронирование
    #path('contact/', views.contact, name='contact'),  # Обратная Связь
    path('contact/', views.Message_Create.as_view(), name='contact'),  # Обратная Связь
    path('reservations/email_confirm/<str:token>', views.reservation_confirm , name='email-confirm'),  # Ссылка для подтверждения брони
]
