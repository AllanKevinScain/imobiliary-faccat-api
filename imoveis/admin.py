from django.contrib import admin
from .models import Imovel


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'endereco',)
    search_fields = ('nome', 'endereco',)
    list_filter = ('tipo',)
