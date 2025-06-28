from django.contrib import admin
from .models import Imovel, Quarto, Reserva


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'endereco',
                    'cidade', 'estado', 'disponivel')
    search_fields = ('nome', 'endereco', 'cidade', 'disponivel', 'estado')
    list_filter = ('tipo', 'disponivel')


@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'nome')
    search_fields = ('imovel__nome', 'nome')
    list_filter = ('imovel__tipo',)


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'funcionario',
                    'data_inicio', 'data_fim',)
    search_fields = ('imovel__nome', 'cliente__nome', 'funcionario__nome')
    list_filter = ('data_inicio', 'data_fim')
