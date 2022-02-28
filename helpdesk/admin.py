from django.contrib import admin
from .models import Solicitantes, Solicitacoes,  Setores, Locais


class SolicitanteAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class SetorAdmin(admin.ModelAdmin):
    list_display = ('nome',)


class LocalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'setor')


class SolicitacaoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'usuario', 'data_criacao',
                    'data_atualizacao', 'status')


admin.site.register(Solicitantes, SolicitanteAdmin)
admin.site.register(Setores, SetorAdmin)
admin.site.register(Locais, LocalAdmin)
admin.site.register(Solicitacoes, SolicitacaoAdmin)
