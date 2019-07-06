from django.forms import ModelForm
from .models import transacao

class TransacaoForm(ModelForm):
    class Meta:
        model = transacao
        fields = ['data', 'descricao', 'valor', 'observacoes', 'categoria']