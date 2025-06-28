from django.contrib import admin
from .models import Funcionario


@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'cargo')
    search_fields = ('nome', 'email',)
