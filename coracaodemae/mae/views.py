from django.shortcuts import render
from django.contrib.auth.decorators import login_required


#@login_required
def inicio(request):
    context = {}
    return render(request, 'mae/index.html', context)


def login(request):
    context = {}
    return render(request, 'mae/login.html', context)


def cadastro_mae(request):
    context = {}
    return render(request, 'mae/cadastro_mae.html', context)


def lista(request):
    context = {}
    return render(request, 'mae/lista.html', context)


def detalhe(request, param):
    context = {}
    return render(request, 'mae/detalhe.html', context)


def pagamento(request, param):
    context = {}
    return render(request, 'mae/pagamento.html', context)


def confirmacao(request, param):
    context = {}
    return render(request, 'mae/confirmacao.html', context)


def avaliacao(request, param):
    context = {}
    return render(request, 'mae/avaliacao.html', context)
