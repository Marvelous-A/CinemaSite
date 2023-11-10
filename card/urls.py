from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_list, name='main_list'),
    path('tickets_films', views.tickets_films, name='tickets_films'),
    path('add_move', views.add_move, name='add_move'),
    path('film_detal/<int:pk>/', views.film_detal, name='film_detal')
]