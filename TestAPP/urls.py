from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('login_api', views.login_api),
    path('home', views.home, name='home'),
]