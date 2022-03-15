from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from .forms import SolicitacaoForm
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from helpdesk.models import Solicitacao


class SolicitacaoCreateView(CreateView):
    model = Solicitacao
    fields = ['descricao', 'usuario', 'local',
              'solicitante', 'status', 'patrimonio', 'resposta']
    reverse_lazy = 'solicitacao-list'
    success_url = '/'


class SolicitacaoListView(ListView):
    model = Solicitacao
    ordering = ['-data_criacao']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SolicitacaoForm()
        return context


class SolicitacaoUpdateView(UpdateView):
    model = Solicitacao
    fields = ['descricao', 'usuario', 'local',
              'solicitante', 'status', 'patrimonio', 'resposta']
    template_name = 'helpdesk/solicitacao_form.html'

    def get_success_url(self):
        return redirect('solicitacao-list')
