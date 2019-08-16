from django.shortcuts import render
from django.http import HttpResponse
from website.models import Desenvolvedor, Instituicao, Projeto

# Create your views here.


def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)


def cadastroDev(request):
    contexto = {}
    if request.method == 'POST':
        dev = Desenvolvedor()
        dev.nome = request.POST.get('nome')
        dev.genero = request.POST.get('genero')
        dev.interesse = request.POST.get('interesse')
        dev.telefone = request.POST.get('telefone')
        dev.email = request.POST.get('email')
        dev.senha = request.POST.get('senha')
        dev.save()
        contexto = {
                'msg': 'Cadastro realizado com sucesso'
        }
        return render(request, 'login.html', contexto)

 return render(request, 'cadastro.html', contexto)

def loginDev(request):
        if request.method == 'POST':
                email_form = request.POST.get('email')
                senha_form = request.POST.get('pass')
                login1 = Desenvolvedor.objects.filter(email=email_form).first()
                login2 = Desenvolvedor.objects.filter(senha=senha_form).first()

                if login1 and login2 is None:
                        contexto = {'msg': 'Email ou senha incorretos'}
                        return render(request, 'login.html', contexto)
                else:
                        contexto = {'Desenvolvedor': login1}
                        return render(request, 'sobre.html', contexto)
                return render(request, 'login.html',{})

def cadastroInst(request):
        contexto = {}
        if request.method == 'POST':
               inst = Instituicao()
               inst.nome_inst = request.POST.get('nome')
               inst.segmento = request.POST.get('segmento')
               inst.telefone_inst = request.POST.get('telefone')
               inst.email_inst = request.POST.get('email')
               inst.senha_inst = request.POST.get('senha')
               inst.save()
               contexto = {
                       'msg':'Cadastro realizado com sucesso'
               }
               return render(request, 'login.html', contexto)

 return render(request, 'cadastro.html', contexto)


