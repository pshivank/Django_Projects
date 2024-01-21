from django.urls import path , include 
from . import views

urlpatterns = [
    path(' ' , views.Home , name='home'),
    path('register' , views.Register , name='register'),
    path('login' , views.Login , name='login'),
    path('chathome' , views.ChatHome , name='chathome'),
]