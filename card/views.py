from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Cinema, Hall, Payment, User
from .forms import FilmForm, ProfileForm, PaymentForm, UserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('main_list')  # Перенаправление на главную страницу
        else:
            # Возвращение сообщения об ошибке
            return render(request, 'auth/login.html', {'error': 'Неверное имя пользователя или пароль'})
    else:
        return render(request, 'auth/login.html')

# @login_required(login_url='login')
def main_list(request):
    return render(request, 'card/main_list.html', {})
  

# @login_required(login_url='login')
def tickets_films(request):
    films = Film.objects.all()
    return render(request, 'card/tickets_films.html', {'films': films})

# @login_required(login_url='login')
def film_detal(request, pk):
    films = get_object_or_404(Film, pk=pk)
    cinemas_True = films.cinemas_detals.split(';')
    cinemas = Cinema.objects.all()
    halls = Hall.objects.all()
    return render(request, 'card/film_detal.html', {'films': films, 'cinemas': cinemas, 'cinemas_True': cinemas_True, 'halls': halls})

@login_required(login_url='login')
def add_move(request):
    if request.method == 'POST':
        request.POST = request.POST.copy()
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors.as_data())
        return redirect('main_list')
    else:
        Film.objects.all()
        form = FilmForm()
    return render(request, 'card/add_move.html', {})

@login_required(login_url='login')
def logout_view(request):
    logout(request)
    return render(request, 'card/main_list.html', {})

@login_required(login_url='login')
def hall_detal(request, pk):
    halls = get_object_or_404(Hall, pk=pk)
    places = []
    for i in range(halls.rows):
        row = []
        for j in range(halls.places):
            row.append(f'{i}, {j}')
        places.append(row)
    if request.method == "POST":
        request.POST.get('brone_places')
        request.POST.get('resault_price')
        form_payment = PaymentForm(request.POST)
        if form_payment.is_valid():
            form_payment.save()
        else:
            print(form_payment.errors.as_data())
        return redirect('pay')
    return render(request, 'card/hall_detal.html', {'halls': halls, 'places': places})

def pay(request):
    return render(request, 'payment/pay.html', {})

def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            login(request, user)

            return redirect('main_list')
        else:
            print(user_form.error_messages)
            print(profile_form.error_messages)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
     
    context = {
        user_form: user_form,
        profile_form: profile_form
    }
    return render(request, 'auth/register.html')
@login_required
def update_profile(request):
    return render(request, 'auth/update_profile.html', {})