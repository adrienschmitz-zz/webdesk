from django.shortcuts import redirect, render
from helpdesk.models import Solicitacao
from .forms import SolicitacaoForm


def index(request):
    return render(request, 'helpdesk/index.html', {'solicitacoes': Solicitacao.objects.all()})


def nova_solicitacao(request, solicitacao_id):
    if request.method == 'POST':
        form = SolicitacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SolicitacaoForm()
    return render(request, 'helpdesk/nova_solicitacao.html', {'form': form})
