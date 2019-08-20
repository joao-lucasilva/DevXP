from django.shortcuts import render, redirect
from django.http import HttpResponse
from website.models import Desenvolvedor, Instituicao, Projeto

# Create your views here.


def index(request):
    contexto = {}
    return render(request, 'index.html', contexto)

def sobre(request):
        contexto = {}
        return render(request, 'sobre.html', contexto)

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
                        msg = {'msg': 'Email ou senha incorretos'}
                        return render(request, 'login.html', msg)
                else:
                        msg = {'instituicao': login1}                   
                        return redirect('http://localhost:8000/listardev')
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
               return render(request, 'loginst.html', contexto)

        return render(request, 'cadinst.html', contexto)

def loginInst(request):
        if request.method == 'POST':
                email_form = request.POST.get('email')
                senha_form = request.POST.get('pass')
                login1 = Instituicao.objects.filter(email_inst=email_form).first()
                login2 = Instituicao.objects.filter(senha_inst=senha_form).first()

                if login1 and login2 is None:
                        msg = {'msg': 'Email ou senha inválidos'}
                        return render(request, 'loginst.html', msg)
                else:
                        msg = {'instituicao': login1}
                        print('Login sucess')
                        return render(request, 'cadastrarideia.html', msg)
        return render(request, 'loginst.html', {})
                
def cadastrarProjeto(request):
        if request.method == 'POST':
                inst = request.POST.get('inst')
                inst = Instituicao.objects.filter(nome_inst=inst).first()
                print(inst)
                if inst is not None:
                        proj = Projeto()
                        proj.instituicao  = inst
                        proj.nome_projeto = request.POST.get('nome')
                        proj.descricao = request.POST.get('descricao')
                        proj.save()
                        msg = {'msg':'Cadastrado com Sucesso!'}
                        return redirect('http://localhost:8000/listar')
        msg = {'msg':'Erro ao cadastrar'}
        return render(request, 'cadastrarideia.html', {})

def listarProjetos(request):
        projetos = Projeto.objects.filter(ativo=True).all()
        contexto = {
                'projetos':projetos
        }
        return render(request, 'listar.html', contexto)


def listarDev(request):
        projetos = Projeto.objects.filter(ativo=True).all()
        contexto = {
            'projetos': projetos
        }
        return render(request, 'listardev.html', contexto)
