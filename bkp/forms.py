import datetime
from django import forms
from .models import Solicitacao


class SolicitacaoForm(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = [
            'descricao',
            'usuario',
            'local',
            'solicitante',

            'status',
            'patrimonio',
            'resposta'
        ]

        widgets = {
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
            'patrimonio': forms.TextInput(attrs={'class': 'form-control'}),
            'solicitante': forms.Select(attrs={'class': 'form-control'}),
            'resposta': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'local': forms.Select(attrs={'class': 'form-control'}),
        }
