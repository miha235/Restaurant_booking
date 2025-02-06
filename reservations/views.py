import secrets

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from users.models import User
from .models import Reservation, Table, Message
from django.core.mail import send_mail
from django.conf import settings
from .forms import ReservationForm, MessageForm
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView


def index(request):
    """Главная страница."""
    return render(request, 'index.html')

def about(request):
    """Страница "О ресторане"."""
    return render(request, 'about.html')

class Reservation_Create(LoginRequiredMixin, CreateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_form.html'
    #fields = ("name", "description", "image", "price", "category")

    def form_valid(self, form):
        reservation = form.save()
        reservation.user_id = self.request.user
        reservation.save()
        return super(Reservation_Create, self).form_valid(form)

class Reservation_Update(LoginRequiredMixin, UpdateView):
    model = Reservation
    form_class = ReservationForm
    template_name = 'reservation_form.html'
    #fields = ("date", "time", "guests", "table")
    success_url = reverse_lazy ('profile' )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        return form

    def form_valid(self, form):
        reservation = self.object
        reservation.user_id = self.request.user
        #print(form.instance.id, self.kwargs['pk'])
        #super(Reservation_Update, self).save(form)
        reservation.save()
        return super(Reservation_Update, self).form_valid(form)

# def reservation_view(request, id):
#     """Страница бронирования."""
#     reservation = Reservation.objects.filter(id=id).first()
#     if request.method == 'POST':
#         # Логика обработки данных бронирования
#         date = request.POST.get('date')
#         time = request.POST.get('time')
#         guests = request.POST.get('guests')
#         # Обработайте данные бронирования (например, сохраните в БД)
#         return render(request, 'reservations.html', {'success': True, 'date': date, 'time': time, 'guests': guests})
#     return render(request, 'reservations.html')

def reservation_update(request, id):
    res = Reservation.objects.filter(id=id).first()
    """Страница бронирования."""
    print(res.id, res.date, res.table)
    return render(request, 'reservations.html', {'success': True, 'date': res.date, 'time': res.time, 'guests': res.guests, 'table': res.table})

def reservation_delete(request, id):
    print(id)
    res = Reservation.objects.filter(id=id).delete()
    res = Reservation.objects.filter(user=request.user)
    """Страница бронирования."""
    return render(request, 'profile.html', {'reservations': res})


def book(request):
    ''' Функция бронирования столика
    Пользователь выбирает дату, время, указывает количество человек и желаемый столик.
    Если
    '''
    if request.method == 'POST':
        # Извлекаем данные из формы
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        table = request.POST.get('table')

        # добавить отправку уведомления
        selected_table = Table.objects.filter(number=int(table)).first()

        print(selected_table)
        user_id = request.user.id

        reservation = Reservation.objects.create(date=date, time=time, table_id=selected_table.id, user_id=user_id) # временно - без привзяки к пользователю


        # Отправка письма с информацией о бронировании
        token = secrets.token_hex(16) # verification_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        reservation.token = token
        reservation.save()
        host = request.get_host()
        url = f'http://{host}/reservations/email_confirm/{token}'
        try:
            send_mail(
                'Бронирование ',
                f'Ваше бронирование в Work & Dine:\nCтолик № {table}\nВремя: {date} в {time}\nГостей: {guests} чел.'
                f'\n\nДля подтверждения брони пройдети по ссылке {url}',
                settings.EMAIL_HOST_USER,  # Email отправителя из settings.py
                [request.user.email],  # Email получателя
                fail_silently=False,
            )
            print()
        except Exception as e:
            # Логирование или обработка ошибки
            print(f"Ошибка при отправке письма с деталями брони: {e}")


        # После успешного бронирования перенаправляем на страницу успеха
        return render(request, 'reservation_success.html', {
            'date': date,
            'time': time,
            'guests': guests,
        })

    # Если запрос не POST, перенаправляем на страницу бронирования
    return redirect('reservation')

def reservation_confirm(request, token):
    print(token)
    reservation = get_object_or_404(Reservation, token=token)
    print(reservation, ' - бронирование подтверждено')
    reservation.is_confirmed = True
    reservation.save()
    return redirect(reverse("profile"))

def profile(request):
    """Личный кабинет."""
    # Пример данных о бронированиях
    user_id = request.user.id
    reservations = Reservation.objects.filter(user=user_id, is_confirmed=True)

    return render(request, 'profile.html', {'reservations': reservations})

# def contact(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         message = request.POST.get('message')
#         # Здесь можно обработать или сохранить данные формы
#
#         return HttpResponse("Спасибо за ваше сообщение!")
#     return render(request, 'contact.html')  # Возвращаем форму на странице

class Message_Create(CreateView): # Без LoginRequiredMixin - незарегистрированные пользователи тоже могут писать.
    model = Message
    form_class = MessageForm
    template_name = 'contact.html'
    success_url = reverse_lazy('index')
    #fields = ("name", "email", "text")

    # def form_valid(self, form):
    #     print('!')
    #     user_ = self.request.user.id
    #     form.user = user_ if user_ else MANAGER_ID
    #     message = form.save(commit=False)
    #     print(message)
    #     if self.request.user is not None:
    #         user_ = User.objects.filter(user=user_).first()
    #         message.email = user_.email
    #         message.name = user_.first_name + user_.last_name
    #     message.save()
    #     return super(Message_Create, self).form_valid(form)


# def tables_available(request):
#     times =
#     tables = Table.objects.filter()