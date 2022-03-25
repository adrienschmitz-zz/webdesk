from re import template
from django.shortcuts import redirect, render
from .forms import SolicitacaoForm
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from helpdesk.models import Solicitacao
from helpdesk.models import Status


class SolicitacaoListView(ListView):
    model = Solicitacao
    form = SolicitacaoForm()
    ordering = ['-data_criacao']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'status_list': Status.objects.all().order_by('id')
        })
        context['form'] = SolicitacaoForm()
        return context


class SolicitacaoCreateView(CreateView):
    model = Solicitacao
    form = SolicitacaoForm()
    fields = ('descricao', 'usuario', 'local',
              'solicitante', 'status', 'patrimonio', 'resposta')
    template_name = 'helpdesk/solicitacao_create.html'
    success_url = '/'


class SolicitacaoUpdateView(UpdateView):
    model = Solicitacao
    fields = ('descricao', 'usuario', 'local',
              'solicitante', 'status', 'patrimonio', 'resposta')
    template_name = 'helpdesk/solicitacao_form.html'
    success_url = '/'
