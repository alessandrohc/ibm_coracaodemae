from django.contrib import admin
from .models import *


class ImagensInlineAdmin(admin.StackedInline):
    model = Imagens
    extra = 1


class FilhoInlineAdmin(admin.StackedInline):
    model = Filho
    extra = 1


class PostsInlineAdmin(admin.StackedInline):
    model = Posts
    extra = 1


class FriendsInlineAdmin(admin.StackedInline):
    model = Friends
    extra = 1


class ApoioMaeFilhosAdmin(admin.StackedInline):
    model = ApoioMaeFilhos
    extra = 1


class MaeAdmin(admin.ModelAdmin):
    exclude = ('about_me', 'website_url', 'blog_url', 'date_of_birth', 'gender', 'raw_data', 'image')
    inlines = [FilhoInlineAdmin, ImagensInlineAdmin, FriendsInlineAdmin, PostsInlineAdmin]
    list_display = ('nome', 'user', 'facebook_id')


class ComentarioMaeAdmin(admin.ModelAdmin):
    list_display = ('mae_origem', 'mae_destino', 'comentario')


class AvaliacaoMaeAdmin(admin.ModelAdmin):
    list_display = ('mae_origem', 'mae_destino', 'avaliacao')


class ApoioMaeAdmin(admin.ModelAdmin):
    list_display = ('mae_origem', 'mae_destino', 'foi_processado')
    inlines = [ApoioMaeFilhosAdmin]


admin.site.register(Mae, MaeAdmin)
admin.site.register(ComentarioMae, ComentarioMaeAdmin)
admin.site.register(AvaliacaoMae, AvaliacaoMaeAdmin)
admin.site.register(ApoioMae, ApoioMaeAdmin)
