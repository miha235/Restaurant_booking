from django.http import HttpResponse
from django.shortcuts import render,redirect


def index(request):
    """Главная страница."""
    return render(request, 'index.html')

def about(request):
    """Страница "О ресторане"."""
    return render(request, 'about.html')

def reservation(request):
    """Страница бронирования."""
    if request.method == 'POST':
        # Логика обработки данных бронирования
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        # Обработайте данные бронирования (например, сохраните в БД)
        return render(request, 'reservations.html', {'success': True, 'date': date, 'time': time, 'guests': guests})
    return render(request, 'reservations.html')

def book(request):
    if request.method == 'POST':
        # Извлекаем данные из формы
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')

        # Здесь можно добавить сохранение данных в базу или отправку уведомления
        # Например:
        # Reservation.objects.create(date=date, time=time, guests=guests)

        # После успешного бронирования перенаправляем на страницу успеха
        return render(request, 'reservation_success.html', {
            'date': date,
            'time': time,
            'guests': guests,
        })

    # Если запрос не POST, перенаправляем на страницу бронирования
    return redirect('reservation')

def profile(request):
    """Личный кабинет."""
    # Пример данных о бронированиях
    bookings = [
        {'date': '2025-01-23', 'time': '12:00', 'table': 5},
        {'date': '2025-01-20', 'time': '15:00', 'table': 3},
    ]
    return render(request, 'profile.html', {'bookings': bookings})
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        # Здесь можно обработать или сохранить данные формы
        return HttpResponse("Спасибо за ваше сообщение!")
    return render(request, 'contact.html')  # Возвращаем форму на странице
