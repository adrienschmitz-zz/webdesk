from django.db import models


class usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class solicitante(models.Model):
    nome = models.CharField(max_length=100)


class solicitacoes(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(usuarios, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default='Aberto')


class perfis(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()


class setores(models.Model):
    nome = models.CharField(max_length=100)


class locais(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(setores, on_delete=models.CASCADE)
