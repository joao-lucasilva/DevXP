from django.urls import path, include
from website.views import index, sobre ,cadastroDev, cadastroInst, loginDev, loginInst, cadastrarProjeto, listarProjetos

urlpatterns = [
    path('index', index),
    path('cadastro', cadastroDev),
    path('login', loginDev),
    path('cadinst', cadastroInst),
    path('loginst', loginInst),
    path('sobre', sobre),
    path('listar', listarProjetos),
    path('cadastrar_projeto', cadastrarProjeto)
]