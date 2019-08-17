from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('cadastro.html', views.cadastroDev),
    path('login.html', views.loginDev)
]