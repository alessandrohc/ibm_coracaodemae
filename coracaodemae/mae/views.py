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


def contexto_para_mae(mae_obj, user=None):
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

    if user:
        mae_origem = user.mae
        context['amigas_comum'] = mae_obj.get_amigas_em_comum(mae_origem)
        context['itens_comum'] = mae_obj.get_itens_em_comum(mae_origem)

    return context


class Inicio(View, ContextMixin):

    template_name = 'mae/index.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(**kwargs)
        context['autosubmit'] = False

        self.request.session['date_apoio'] = self.request.POST['date_apoio']

        m = Mae.objects.get(user=self.request.user)

        maes = sorted(Mae.objects.all().exclude(pk=m.pk), key=lambda x: x.get_order_watson(m))

        for mae in maes:
            context['maes'].append(contexto_para_mae(mae, self.request.user))

        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)

        context['user'] = self.request.user
        context['maes'] = []
        context['autosubmit'] = True

        m = Mae.objects.get(user=self.request.user)

        context['filhos'] = m.filho_set.all()

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
        context['mae'] = contexto_para_mae(mae_obj, self.request.user)

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
        context['user'] = self.request.user

        return context


class Chat(View, ContextMixin):

    template_name = 'mae/chat.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return render(request, self.template_name, context)

    def get_context_data(self, **kwargs):
        context = super(Chat, self).get_context_data(**kwargs)
        context['user'] = self.request.user

        return context
