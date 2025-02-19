from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('registration/', views.registration, name='registration'),
    path('users-cart/', views.users_cart, name='users_cart'),
    path('profile/', views.profile, name='profile'),
]