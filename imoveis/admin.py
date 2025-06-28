from django.contrib import admin
from .models import Imovel, Quarto, Reserva


@admin.register(Imovel)
class ImovelAdmin(admin.ModelAdmin):
    list_display = ('nome', 'tipo', 'endereco',
                    'cidade', 'estado')
    search_fields = ('nome', 'endereco', 'cidade', 'estado')
    list_filter = ('tipo',)


@admin.register(Quarto)
class QuartoAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'nome', 'disponibilidade')
    search_fields = ('imovel__nome', 'nome')
    list_filter = ('imovel__tipo', 'disponibilidade')


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('quarto', 'cliente', 'data_inicio', 'data_fim',)
    search_fields = ('quarto__nome', 'cliente__nome',)
    list_filter = ('data_inicio', 'data_fim')
