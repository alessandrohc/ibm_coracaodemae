from django.contrib import admin
from .models import *


class MaeAdmin(admin.ModelAdmin):
    exclude = ('about_me', 'website_url', 'blog_url', 'date_of_birth', 'gender', 'raw_data', 'image')


admin.site.register(Mae, MaeAdmin)
