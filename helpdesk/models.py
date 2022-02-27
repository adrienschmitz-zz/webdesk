from django.db import models


class Usuarios(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)


class Solicitantes(models.Model):
    nome = models.CharField(max_length=100)


class Solicitacoes(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default='Aberto')


class Perfis(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()


class Setores(models.Model):
    nome = models.CharField(max_length=100)


class Locais(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE)
