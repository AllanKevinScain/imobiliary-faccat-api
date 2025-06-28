from django.contrib import admin
from .models import Cliente


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cpf', 'data_nascimento')
    search_fields = ('nome', 'email', 'cpf')
    list_filter = ('data_nascimento', 'cpf')
