from django.shortcuts import render, redirect, get_object_or_404
from .models import Film, Cinema, Hall
from .forms import FilmForm, RegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required


# def base(request):
#     return render(request, 'card/main_list.html', {})
@login_required(login_url='login')
def main_list(request):
    if request.user.is_authenticated:
        return render(request, 'card/main_list.html', {})
    else:
        return render(request, 'card/login.html', {})

@login_required(login_url='login')
def tickets_films(request):
    films = Film.objects.all()
    return render(request, 'card/tickets_films.html', {'films': films})

@login_required(login_url='login')
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
def logout(request):
    return render(request, 'card/main_list.html', {})

# def register(request):
#     if request.method == 'POST':
#         form = RegisterForm(request.Post)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('main_list')
#     else:
#         form = RegisterForm()
#     return render(request,'auth/register.html', {"form": form})

# TODO: Дописать отображение для логина