from django.contrib import admin
from .models import Table, Reservation

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'created_at')


