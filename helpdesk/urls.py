from django.urls import path
from helpdesk.views import SolicitacaoListView, SolicitacaoUpdateView, SolicitacaoCreateView


urlpatterns = [
    path('', SolicitacaoListView.as_view(), name='solicitacao-list'),
    path('solicitacao_create/', SolicitacaoCreateView.as_view(),
         name='solicitacao-create'),
    path('<pk>/solicitacao_form', SolicitacaoUpdateView.as_view(),
         name='solicitacao-form'),
]
