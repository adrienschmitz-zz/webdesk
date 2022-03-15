from django.db import models
from django.contrib.auth.models import User


class Status(models.Model):
    nome = models.CharField(max_length=100)
    cor = models.CharField(max_length=7, default='#000000')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Status'
        verbose_name_plural = "Status"


class Setor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = "Setores"


class Local(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = "Locais"


class Solicitante(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = "Solicitantes"


class Solicitacao(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.ForeignKey(Local, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(
        Solicitante, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    patrimonio = models.CharField(max_length=100, blank=True)
    resposta = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = "Solicitações"
