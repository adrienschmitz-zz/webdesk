from django.contrib import admin
from .models import Usuarios, Solicitantes, Solicitacoes, Perfis, Setores, Locais


class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = "Usuarios"


class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    class Meta:
        verbose_name = 'Solicitante'
        verbose_name_plural = "Solicitantes"


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'usuario', 'data_criacao',
                    'data_atualizacao', 'status')

    class Meta:
        verbose_name = 'Solicitação'
        verbose_name_plural = "Solicitações"


class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = "Perfis"


class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome',)

    class Meta:
        verbose_name = 'Setor'
        verbose_name_plural = "Setores"


class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor')

    class Meta:
        verbose_name = 'Local'
        verbose_name_plural = "Locais"


admin.site.register(Usuarios, UsuarioAdmin)
admin.site.register(Solicitantes, SolicitanteAdmin)
admin.site.register(Solicitacoes, SolicitacaoAdmin)
admin.site.register(Perfis, PerfilAdmin)
admin.site.register(Setores, SetorAdmin)
admin.site.register(Locais, LocalAdmin)
