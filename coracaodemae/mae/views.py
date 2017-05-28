from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView, ListView, View, TemplateView, DetailView
from django.views.generic.base import ContextMixin

from mae.models import *
from django.db.models import Avg, Count, Sum
from django.core.urlresolvers import reverse


def extract_mae_id(**kwargs):
    mae_id = kwargs.pop('mae_id', None)
    print(mae_id)
    mae_obj = Mae.objects.get(pk=mae_id)
    return mae_id, mae_obj


def contexto_para_mae(mae_obj):
    context = {}
    context['obj'] = mae_obj
    context['qtd_filho'] = mae_obj.filho_set.count()
    context['comentarios'] = ComentarioMae.objects.filter(mae_destino=mae_obj)
    aggregates = AvaliacaoMae.objects.filter(mae_destino=mae_obj).aggregate(
        total=Sum('avaliacao'), average=Avg('avaliacao'), count=Count('avaliacao'))
    # count = aggregates.get('count') or 0
    # total = aggregates.get('total') or 0
    average = aggregates.get('average') or 0.0
    context['avaliacao'] = str(average).replace(",", ".")
    return context


class Inicio(ListView):
    """
    Url para Exibir os detalhes do Post
    """
    model = Mae

    template_name = 'mae/index.html'

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)

        context['user'] = self.request.user
        context['maes'] = []

        m = Mae.objects.get(user=self.request.user)

        maes = sorted(Mae.objects.all(), key=lambda x: x.get_order_watson(m))

        for mae in maes:
            context['maes'].append(contexto_para_mae(mae))

        return context


class Detalhe(View, ContextMixin):

    template_name = 'mae/detalhe.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(Detalhe, self).get_context_data(**kwargs)
        mae_id, mae_obj = extract_mae_id(**kwargs)
        context['user'] = self.request.user
        context['mae'] = contexto_para_mae(mae_obj)

        return context


class Pagamento(View, ContextMixin):

    template_name = 'mae/pagamento.html'

    def post(self, request, *args, **kwargs):
        mae_id, mae_obj = extract_mae_id(**kwargs)
        # context = self.get_context_data(**kwargs)
        return redirect(reverse('confirmacao', kwargs={'mae_id': mae_id}))

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(Pagamento, self).get_context_data(**kwargs)
        mae_id, mae_obj = extract_mae_id(**kwargs)
        context['user'] = self.request.user
        context['mae'] = contexto_para_mae(mae_obj)

        return context


class Confirmacao(View, ContextMixin):

    template_name = 'mae/confirmacao.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(Confirmacao, self).get_context_data(**kwargs)
        mae_id, mae_obj = extract_mae_id(**kwargs)
        context['user'] = self.request.user
        context['mae'] = contexto_para_mae(mae_obj)

        return context


class LightboxAvaliacao(View, ContextMixin):

    template_name = 'mae/lightbox_avaliacao.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(LightboxAvaliacao, self).get_context_data(**kwargs)
        mae_id, mae_obj = extract_mae_id(**kwargs)
        context['user'] = self.request.user
        context['mae'] = contexto_para_mae(mae_obj)

        return context


class LightboxNotificacao(View, ContextMixin):

    template_name = 'mae/lightbox_notificacao.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(LightboxNotificacao, self).get_context_data(**kwargs)
        mae_id, mae_obj = extract_mae_id(**kwargs)
        context['user'] = self.request.user
        context['mae'] = contexto_para_mae(mae_obj)

        return context
