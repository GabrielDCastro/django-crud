from django.shortcuts import render
from .models import transacao
import datetime

def listagem(request):
    data={}
    data['transacoes'] = transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

# Create your views here.
