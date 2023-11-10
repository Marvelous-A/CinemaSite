from django.shortcuts import render, redirect, get_object_or_404
from .models import Film
from .forms import FilmForm, RegisterForm
from django.contrib.auth import login, authenticate


# def base(request):
#     return render(request, 'card/main_list.html', {})

def main_list(request):
    return render(request, 'card/main_list.html', {})

def tickets_films(request):
    films = Film.objects.all()
    return render(request, 'card/tickets_films.html', {'films': films})

def film_detal(request, pk):
    films = get_object_or_404(Film, pk=pk)
    return render(request, 'card/film_detal.html', {'films': films})

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

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.Post)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('main_list')
        else:
            form = RegisterForm()
    return render(request,'card/register.html', {"form": form})

# TODO: Дописать отображение для логина