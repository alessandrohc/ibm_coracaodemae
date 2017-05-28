from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.contrib import admin
from mae import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_required(views.Inicio.as_view()), name='inicio'),
    url(r'^detalhe/(?P<mae_id>[0-9]+)/$', login_required(views.Detalhe.as_view()), name='detalhe'),
    url(r'^pagamento/(?P<mae_id>[0-9]+)/$', login_required(views.Pagamento.as_view()), name='pagamento'),
    url(r'^confirmacao/(?P<mae_id>[0-9]+)/$', login_required(views.Confirmacao.as_view()), name='confirmacao'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'mae/login.html'}, name="login"),
    url(r'^accounts/logout/$', auth_views.logout, {'next_page': '/'}, name="logout"),
    # url(r'^cadastro_mae/$', views.cadastro_mae),
    url(r'^lightbox/avaliacao/(?P<mae_id>[0-9]+)/$',
        login_required(views.LightboxAvaliacao.as_view()), name='lightbox_avaliacao'),
    url(r'^lightbox/notificacao/$',
        login_required(views.LightboxNotificacao.as_view()), name='lightbox_notificacao'),
    url(r'^chat/$', login_required(views.Chat.as_view()), name='chat'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
