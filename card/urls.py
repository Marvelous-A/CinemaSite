from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#TODO: если пользователь не авторизован, то при любой попытке зайти на любую другую страницу сайта должно перекидывать на login форму
urlpatterns = [
    path('', views.main_list, name='main_list'), 
    path('add_move', views.add_move, name='add_move'),
    path('film_detal/<int:pk>/', views.film_detal, name='film_detal'),
    path('hall_detal/<int:pk>/', views.hall_detal, name='hall_detal'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('register', views.register , name='register'),
    path('pay', views.pay, name='pay'),
    path('update_profile', views.update_profile, name='update_profile'),
    path('profile', views.profile, name='profile'),
    path('cinema_detal/<int:pk>/', views.cinema_detal, name='cinema_detal'),
    path('cinemas', views.cinemas, name='cinemas'),
]