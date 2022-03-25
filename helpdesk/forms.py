import datetime
from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Row, Column, Button
from crispy_forms.bootstrap import FormActions
from .models import Solicitacao


class SolicitacaoForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(SolicitacaoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(
            Submit('submit', 'Salvar', css_class='btn-primary'))
        self.helper.form_method = 'POST'

        self.helper.layout = Layout(
            'descricao',
            Row(
                Column('solicitante', css_class='form-group col-md-6 mb-0'),
                Column('local', css_class='form-group'),
                css_class='form-row'
            ),
            Row(
                Column('status', css_class='form-group col-md-6 mb-0'),
                Column('patrimonio', css_class='form-group'),
                css_class='form-row'

            ),
            Row(
                Column('usuario', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'resposta',
            FormActions(
                Submit('save', 'Save changes'),
                Button('cancel', 'Cancel')
            )
        )

    class Meta:
        model = Solicitacao
        fields = (
            'descricao',
            'usuario',
            'local',
            'solicitante',
            'status',
            'patrimonio',
            'resposta'
        )
