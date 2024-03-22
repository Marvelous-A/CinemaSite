from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

#TODO: если пользователь не авторизован, то при любой попытке зайти на любую другую страницу сайта должно перекидывать на login форму
urlpatterns = [
    path('', views.main_list, name='main_list'), 
    
    # Панель для содрудников
    path('manage/', views.manage, name='manage_page'),
    # Менеджинг фильмов
    path('manage/films', views.film_list, name='film_list' ),
    path('manage/films/add', views.add_move, name='add_move'),
    path('manage/films/<int:pk>/edit', views.film_update, name='film_update'),
    path('manage/films/<int:pk>/delete', views.film_delete, name='film_delete'),

    # Рассписание
    path('manage/screening', views.screening_list, name='screening_list'),
    path('manage/screening/add', views.add_screening, name='add_screening'),
    path('manage/screening/<int:pk>/edit',views.screening_update, name='screening_update'),
    path('manage/screening/<int:pk>/delete',views.screening_delete, name='screening_delete'),
    
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