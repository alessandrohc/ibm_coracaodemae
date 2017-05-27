from django.contrib import admin
from .models import *

class ImagensInlineAdmin(admin.StackedInline):
    model = Imagens
    extra = 1

class ImagensAdmin(admin.ModelAdmin):
    pass


class FilhoInlineAdmin(admin.StackedInline):
    model = Filho
    extra = 1


class MaeAdmin(admin.ModelAdmin):
    exclude = ('about_me', 'website_url', 'blog_url', 'date_of_birth', 'gender', 'raw_data', 'image')
    inlines = [FilhoInlineAdmin,ImagensInlineAdmin]


class FilhoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Mae, MaeAdmin)
admin.site.register(Filho, FilhoAdmin)
admin.site.register(Imagens, ImagensAdmin)