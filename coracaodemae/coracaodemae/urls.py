from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from mae import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(views.Inicio.as_view()), name='inicio'),
    url(r'^detalhe/(?P<mae_id>[0-9]+)/$', login_required(views.Detalhe.as_view()), name='detalhe'),
    url(r'^pagamento/(?P<mae_id>[0-9]+)/$', login_required(views.Pagamento.as_view()), name = 'pagamento'),
    url(r'^confirmacao/(?P<mae_id>[0-9]+)/$', login_required(views.Confirmacao.as_view()), name='confirmacao'),

    # url(r'^accounts/login/$', views.login),
    # url(r'^cadastro_mae/$', views.cadastro_mae),
    # url(r'^lista/$', views.lista),
    url(r'^avaliacao/(?P<mae_id>[0-9]+)/$', views.avaliacao),
]
