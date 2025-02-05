# Restraurant_project/restaurant_booking/config/urls.py
from django.contrib import admin
from django.urls import path, include
from reservations import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('reservations.urls')),
    path('users/', include('users.urls')),
]
