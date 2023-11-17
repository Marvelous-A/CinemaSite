from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#TODO: если пользователь не авторизован, то при любой попытке зайти на любую другую страницу сайта должно перекидывать на login форму
urlpatterns = [
    path('', views.main_list, name='main_list'), 
    path('tickets_films', views.tickets_films, name='tickets_films'),
    path('add_move', views.add_move, name='add_move'),
    path('film_detal/<int:pk>/', views.film_detal, name='film_detal'),
    path('hall_detal/<int:pk>/', views.hall_detal, name='hall_detal'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    #path('register/', views.register, name='register')
]