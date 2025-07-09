from django.contrib import admin
from .models import Imovel, Reserva


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'endereco',)
    search_fields = ('nome', 'endereco',)
    list_filter = ('tipo',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'data_inicio', 'data_fim',)
    search_fields = ('imovel__nome', 'cliente__nome',)
    list_filter = ('data_inicio', 'data_fim')
