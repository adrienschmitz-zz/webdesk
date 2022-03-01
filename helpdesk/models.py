from django.db import models
from django.contrib.auth.models import User


class Setores(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = "Setores"


class Locais(models.Model):
    nome = models.CharField(max_length=100)
    setor = models.ForeignKey(Setores, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = "Locais"


class Solicitantes(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = "Solicitantes"


class Solicitacoes(models.Model):
    descricao = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    local = models.ForeignKey(Locais, on_delete=models.CASCADE)
    solicitante = models.ForeignKey(
        Solicitantes, on_delete=models.CASCADE)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=100, default='Aberto')
    patrimonio = models.CharField(max_length=100)
    resposta = models.TextField()

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = "Solicitações"
