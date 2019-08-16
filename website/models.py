from django.db import models

# Create your models here.
class Desenvolvedor(models.Model):
    GENEROS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outros'),
    )
    INTERESSE = (
        ('Front-End', 'Front-End'),
        ('Back-End', 'Back-End'),
        ('Mobile', 'Mobile'),
        ('Full Stack', 'Full Stack'),
        ('Data Science', 'Data Science')
    )
    nome = models.CharField(
        max_length=255,
        verbose_name = 'Nome'
    )
    genero = models.CharField(
        max_length=255,
        verbose_name='Gênero',
        choices=GENEROS
    )
    interesse = models.CharField(
        max_length=255,
        verbose_name='Interesse',
        choices=INTERESSE
    )
    telefone = models.CharField(
        max_length=25,
        verbose_name='Telefone',
    )
    email = models.EmailField(
        max_length=255,
        verbose_name='Email'
    )
    senha = models.CharField(
        max_length=25,
        verbose_name='Senha'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Instituicao(models.Model):
    SEGMENTO = (
        ('Educacional','Organização não governamental educacional'),
        ('Ambiental','Organização não governamental ambiental'),
        ('Médica','Organização não governamental médica')
    )
    nome_inst = models.CharField(
        max_length=255,
        verbose_name='Nome da Instituição'
    )
    segmento = models.CharField(
        max_length=255,
        verbose_name='Segmento da Instituição',
        choices=SEGMENTO
    )
    telefone_inst = models.CharField(
        max_length=30,
        verbose_name='Telefone da Instituiçao'
    )
    email_inst = models.EmailField(
        max_length=255,
        verbose_name = 'Email da Instituição'
    )
    senha_inst = models.CharField(
        max_length=25,
        verbose_name='Senha'
    )
    data_criacao_inst = models.DateTimeField(auto_now_add=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome_inst

class Projeto(models.Model):
    instituicao = models.ForeignKey(
        Instituicao, on_delete=None
    )
    nome_projeto = models.CharField(
        max_length=255,
        verbose_name='Nome do projeto'
    )
    descricao = models.TextField(
        verbose_name='Descreva seu projeto'
    )
    proposta = models.TextField(
        verbose_name='Faça uma proposta'
    )
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.instituicao + '-'+ self.nome_projeto