from django import forms


from .models import Reservation, Table, Message


class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ["date", "time", "guests", "table"]
        exclude = ("owner",)

    def __str__(self):
        return self.table


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ["name", "email", "text"]
