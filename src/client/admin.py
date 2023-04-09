from django.contrib import admin

from client import models


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')
    list_display_links = ('email',)
