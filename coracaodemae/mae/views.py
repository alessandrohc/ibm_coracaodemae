from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, View, TemplateView, DetailView
from mae.models import *
from django.db.models import Avg, Count, Sum


class Inicio(ListView):
    """
    Url para Exibir os detalhes do Post
    """
    model = Mae

    template_name = 'mae/index.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)

        context['user'] = self.request.user
        context['maes'] = Mae.objects.all()

        return context


class Detalhe(ListView):

    model = Mae

    template_name = 'mae/detalhe.html'

    def get_context_data(self, **kwargs):
        context = super(Detalhe, self).get_context_data(**kwargs)
        mae_id = self.kwargs.pop('mae_id', None)
        mae_obj = Mae.objects.get(pk=mae_id)
        context['user'] = self.request.user
        context['mae'] = mae_obj
        context['qtd_filho'] = mae_obj.filho_set.count()

        context['comentarios'] = ComentarioMae.objects.filter(mae_destino=mae_obj)

        aggregates = AvaliacaoMae.objects.filter(mae_destino=mae_obj).aggregate(
            total=Sum('avaliacao'), average=Avg('avaliacao'), count=Count('avaliacao'))
        # count = aggregates.get('count') or 0
        # total = aggregates.get('total') or 0
        average = aggregates.get('average') or 0.0
        context['avaliacao'] = str(average).replace(",", ".")

        return context


def pagamento(request, param):
    context = {}
    return render(request, 'mae/pagamento.html', context)


def confirmacao(request, param):
    context = {}
    return render(request, 'mae/confirmacao.html', context)


def avaliacao(request, param):
    context = {}
    return render(request, 'mae/avaliacao.html', context)


def login(request):
    context = {}
    return render(request, 'mae/login.html', context)


def cadastro_mae(request):
    context = {}
    return render(request, 'mae/cadastro_mae.html', context)
