from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import FilmForm, ProfileForm, PaymentForm, UserForm, FilterForm, ScreeningForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.db import transaction
import time

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_list')  # Перенаправление на главную страницу
        else:
            # Возвращение сообщения об ошибке
            return render(request, 'auth/login.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'auth/login.html')

def employer_check(user):
    return user.profile.is_employer

@login_required(login_url='login')
def main_list(request):
    films = Film.objects\
        .all()\
        .prefetch_related('category', 'director')
    
    halls = Hall.objects.all()
    cinemas = Cinema.objects.all()
    
    search_query = request.GET.get('search_query', request.session.get('search_query', ''))

    if search_query:
        films = films.filter(title__icontains=search_query)

    Filter = FilterForm(request.GET)
    if Filter.is_valid():
        categories = Filter.cleaned_data.get('categories')
        directors = Filter.cleaned_data.get('directors')
        if categories and directors:
            films = films.filter(category__in=categories, director__in=directors)
        elif categories:
            films = films.filter(category__in=categories)
        elif directors:
            films = films.filter(director__in=directors)
    screenings = Screening.objects.all()
    cinemas_film = {}
    for screening in screenings:
        if screening.film not in cinemas_film:
            cinemas_film[screening.film] = {}
        if screening.cinema not in cinemas_film[screening.film]:
            cinemas_film[screening.film][screening.cinema] = []
        cinemas_film[screening.film][screening.cinema].append(screening)
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'card/main_list.html', {'cinemas_film': cinemas_film, 'films': films, 'filter_form': Filter, 'halls': halls, 'cinemas': cinemas, 'search_query': search_query, 'screenings': screenings, 'menu_items': menu_items})


@login_required(login_url='login')
def film_detal(request, pk):
    film = get_object_or_404(Film, pk=pk)
    cinemas = Cinema.objects.all()
    screenings = Screening.objects.filter(film=film).select_related('cinema', 'hall')
    # Сгруппируем сеансы по кинотеатру и залу
    screenings_by_cinema = {}
    for screening in screenings:
        if screening.cinema not in screenings_by_cinema:
            screenings_by_cinema[screening.cinema] = {}
        if screening.hall not in screenings_by_cinema[screening.cinema]:
            screenings_by_cinema[screening.cinema][screening.hall] = []
        screenings_by_cinema[screening.cinema][screening.hall].append(screening)
    return render(request, 'card/film_detal.html', {'film': film, 'screenings_by_cinema': screenings_by_cinema})

@login_required(login_url='login')
def cinemas(request):
    cinemas = Cinema.objects.all()
    screening = Screening.objects.all()
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'card/cinemas.html', {'cinemas': cinemas, 'screening': screening, 'menu_items': menu_items})

@login_required(login_url='login')
def cinema_detal(request, pk):
    cinema = get_object_or_404(Cinema, pk=pk)
    screenings = Screening.objects.filter(cinema=cinema).select_related('cinema', 'hall')
    # Сгруппируем сеансы по кинотеатру и залу
    screenings_by_cinema = {}
    for screening in screenings:
        if screening.cinema not in screenings_by_cinema:
            screenings_by_cinema[screening.cinema] = {}
        if screening.hall not in screenings_by_cinema[screening.cinema]:
            screenings_by_cinema[screening.cinema][screening.hall] = []
        screenings_by_cinema[screening.cinema][screening.hall].append(screening)
    return render(request, 'card/cinema_detal.html', {'screening': screening, 'cinema': cinema, 'screenings_by_cinema': screenings_by_cinema})

##### Manage page
@login_required(login_url='login')
@user_passes_test(employer_check)
def manage(request):
    return render(request, 'manage/main_page.html', {})

##### Manage films

# @transaction.atomic
@login_required(login_url='login')
@user_passes_test(employer_check)
def add_film(request):
    films = Film.objects.all()
    directors = Director.objects.all()
    if request.method == 'POST':
        request.POST = request.POST.copy()
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())
        return redirect('film_list')
    else:
        Film.objects.all()
        form = FilmForm()
    return render(request, 'manage/films/film_form.html', {'film': form, 'directors': directors })

@login_required
@user_passes_test(employer_check)
def film_list(request):
    films = Film.objects.all()
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'manage/films/film_list.html', {'films': films, 'menu_items': menu_items})

@login_required
@user_passes_test(employer_check)
def film_delete(request, pk):
    print(pk)
    film = get_object_or_404(Film, pk=pk)
    print(film)
    if request.method == 'POST':
        film.delete()
        time.sleep(5)
        return redirect('film_list')
    
    return render(request, 'manage/films/delete.html', {'film':film})

@login_required
@user_passes_test(employer_check)
def film_update(request, pk):
    film = get_object_or_404(Film, pk=pk)
    directors = Director.objects.all()
    if request.method == 'POST':
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            print(form)
            return redirect('film_list')
    else:
        form = FilmForm(instance=film)

    return render(request, 'manage/films/film_form.html', {'film': form, 'directors': directors})

@login_required
@user_passes_test(employer_check)
def film_delete(request, pk):
    film = get_object_or_404(Film, pk=pk)
    film.delete()
    time.sleep(2)
    return redirect('film_list')
    
    return render(request, 'manage/films/delete_film.html', {'film':film})

#####

@login_required
@user_passes_test(employer_check)
def screening_list(request):
    screenings = Screening.objects.all()
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'manage/screenings/screening_list.html', {'screenings': screenings, 'menu_items': menu_items})

@login_required
@user_passes_test(employer_check)
def screening_update(request, pk):
    screening = get_object_or_404(Screening, pk=pk)
    return render(request, 'manage/screenings/screening_form.html', {'screening': screening})

@login_required
@user_passes_test(employer_check)
def screening_delete(request, pk):
    screening = get_object_or_404(Screening, pk=pk)
    screening.delete()
    time.sleep(2)
    return redirect('screening_list')
    
    return render(request, 'manage/screenings/delete_screening.html', {'screening':screening})

@login_required
@user_passes_test(employer_check)
def add_screening(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        form = ScreeningForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())
        return redirect('main_list')
    else:
        Screening.objects.all()
        form = ScreeningForm()
    return render(request, 'manage/screenings/screening_form.html', {'screening': form})

#####

@login_required
@user_passes_test(employer_check)
def booking_list(request):
    bookings = Booking.objects.all()
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'manage/bookings/booking_list.html', {'bookings': bookings, 'menu_items': menu_items})

@login_required
@user_passes_test(employer_check)
def delete_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    booking.delete()
    time.sleep(2)
    return redirect('booking_list')
    
    return render(request, 'manage/bookings/delete_booking.html', {})

#####

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return render(request, 'card/main_list.html', {})


@login_required(login_url='login')
def hall_detal(request, pk_hall, pk_screening):
    hall = get_object_or_404(Hall, pk=pk_hall)
    screening = get_object_or_404(Screening, pk=pk_screening)
    places = []
    for i in range(hall.rows):
        row = []
        for j in range(hall.places):
            row.append(f'{i}, {j}')
        places.append(row)
    if request.method == "POST":
        cinema_pk = request.GET.get('cinema_pk')
        hall_pk = request.GET.get('hall_pk')
        film_pk = request.GET.get('film_pk')
        screening_pk = request.GET.get('screening_pk')
        brone_places_str = request.POST.get('brone_places')
        resault_price = request.POST.get('resault_price')

        # Разделение строки по запятой и удаление лишних пробелов
        brone_places_parts = [part.strip() for part in brone_places_str.split(',')]
        # Группировка каждых двух элементов и объединение их в строки с запятой и пробелом
        brone_places = [f"{brone_places_parts[i]}, {brone_places_parts[i+1]}" for i in range(0, len(brone_places_parts), 2)]
        brone_places_ticket = ""
        for i in brone_places:
            brone_places_ticket += f"ряд {int(i[0])+1}, место {int(i[3])+1}; "
        brone_places_ticket = brone_places_ticket[0:-2:]

        form_payment = PaymentForm(request.POST)
        if form_payment.is_valid():
            form_payment.save()
        else:
            print(form_payment.errors.as_data())
        redirect_url = f'/pay_transition/?cinema_pk={cinema_pk}&hall_pk={hall_pk}&film_pk={film_pk}&screening_pk={screening_pk}&brone_places={brone_places}&brone_places_ticket={brone_places_ticket}&resault_price={resault_price}'
        return HttpResponseRedirect(redirect_url)
    import ast
    bookings = Booking.objects.filter(hall=hall)
    booking_pos = []
    for booking in bookings:
        if booking.screening.start_time == screening.start_time:
            for i in ast.literal_eval(booking.position):
                booking_pos.append(i)
    return render(request, 'card/hall_detal.html', {'hall': hall, 'places': places, 'bookings': booking_pos})


def pay_transition(request):
    if request.method == "GET":
        cinema_pk = request.GET.get('cinema_pk')
        hall_pk = request.GET.get('hall_pk')
        film_pk = request.GET.get('film_pk')
        screening_pk = request.GET.get('screening_pk')
        brone_places = request.GET.get('brone_places')
        brone_places_ticket = request.GET.get('brone_places_ticket')

        # print(f"{brone_places=}")
        # print(f"{brone_places_ticket=}")

        resault_price = request.GET.get('resault_price')

        if True: # Проверка на получение оплаты
            booking = Booking(
                user=request.user, 
                cinema=get_object_or_404(Cinema, pk=cinema_pk), 
                hall=get_object_or_404(Hall, pk=hall_pk), 
                film=get_object_or_404(Film, pk=film_pk),
                screening=get_object_or_404(Screening, pk=screening_pk),
                position= brone_places, 
                resault_price = resault_price
                )
            
            booking.save()
        
    return render(request, 'payment/pay_transition.html', {'booking': booking })

def success(request):
    import json, ast
    booking_pk = request.GET.get('booking')
    booking = get_object_or_404(Booking, pk=booking_pk)
    list_pos = ast.literal_eval(booking.position)
    print(f'{list_pos=} {type(list_pos)}')
    brone_places_ticket = " | ".join(list(map(lambda pos: f"Ряд {int(pos.split(',')[0]) + 1}, Место {int(pos.split(',')[1]) + 1}" , list_pos)))
    print(brone_places_ticket)
    return render(request, 'payment/success.html', {"booking": booking, "brone_places_ticket": brone_places_ticket})

@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            # Сохранение данных пользователя
            profile = user.profile
            for field in profile_form.cleaned_data:
                setattr(profile, field, profile_form.cleaned_data[field])
            profile.save()  # то же самое что instance.profile.save() в сигналах

            login(request, user)
            return redirect('main_list')
        else:
            print(user_form.error_messages)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
    context = {
        user_form: user_form,
        profile_form: profile_form
    }
    return render(request, 'auth/register.html')


@login_required
# @transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid() and user_form.is_valid():  # Нужно вводить все параметры включая пороль
            user_form.save()
            profile_form.save()
            # messages.success(request, _('Your profile was successfully updated!'))
            print('Your profile was successfully updated!')
            return redirect('main_list')
        else:
            # messages.error(request, _('Please correct the error below.'))
            print('Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'auth/update_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


@login_required
def profile(request):
    return render(request, 'card/profile.html', {})

@login_required
def delete_transition(request):
    return render(request, 'card/delete_transition.html')








def menu_view(request):
    menu_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'test.html',{"menu_items":menu_items})