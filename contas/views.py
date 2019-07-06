from django.shortcuts import render, redirect
from .models import transacao
from .form import TransacaoForm
import datetime

def listagem(request):
    data={}
    data['transacoes'] = transacao.objects.all()
    return render(request, 'contas/listagem.html', data)

def nova_transacao (request):
    data ={}
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')


    data['form'] = form
    return render(request, 'contas/form.html',  data)

def update(request, pk):
    data={}
    Transacao = transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=Transacao)
    if form.is_valid():
        form.save()
        return redirect('url_listagem')


    data['form'] = form
    data['obj']=Transacao
    return render(request, 'contas/form.html',  data)

def delete(request, pk):
    Transacao =TransacaoForm.objects.get(pk=pk)
    Transacao.delete()
    return redirect('url_listagem')