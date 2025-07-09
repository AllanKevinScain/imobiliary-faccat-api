from django.contrib import admin
from .models import Reserva


@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('imovel', 'cliente', 'data_inicio', 'data_fim',)
    search_fields = ('imovel__nome', 'cliente__nome',)
    list_filter = ('data_inicio', 'data_fim')
