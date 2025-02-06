from django import forms
from django.forms import ModelChoiceField

from .models import Reservation, Table, Message

class ReservationForm (forms.ModelForm):
    #tables = Table.objects.all()
    #print(* tables)
    #table = ModelChoiceField(queryset=tables, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Reservation
        fields = ['date','time','guests','table']
        exclude = ('owner',)


    # def __init__(self, *args, **kwargs):
    #     super(ReservationForm, self).__init__(*args, **kwargs)
    #     self.fields['table'].queryset = Table.objects.all()

    def __str__(self):
        return self.table

    # def __init__(self, *args, **kwargs):
    #     user = kwargs.pop('user', '')
    #     super(Table, self).__init__(*args, **kwargs)
    #     self.fields['description'] = forms.ModelChoiceField(queryset=Table.objects.filter(owner=user))

class MessageForm (forms.ModelForm):

    class Meta:
        model = Message
        fields = ['name','email','text']
        #exclude = ('',)
