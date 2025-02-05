from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Table(models.Model):
    number = models.PositiveIntegerField(unique=True)
    seats = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"Table {self.number} - {self.seats} seats"

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    guests = models.PositiveIntegerField(default=1)
    token = models.CharField(
        max_length=100,
        blank=True,
        null=True,

    )
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"Reservation for {self.user} on {self.date} at {self.time} ({self.guests} person(s)"

class Message(models.Model):
    name = models.TextField(blank=True)
    text = models.TextField(blank=True)
    email = models.EmailField()

    def __str__(self):
        return f"Message from {self.email} : {self.text[:30]}"
