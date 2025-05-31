from django.urls import path
from .views import index, funcionarios, funcionarios_cadastrar, funcionarios_editar
from .views import imoveis, imoveis_cadastrar, imoveis_editar
from .views import clientes, clientes_cadastrar, clientes_editar
from .views import reservas, reservas_cadastrar

urlpatterns = [
    path('', index, name='index'),

    path('funcionarios/', funcionarios, name='funcionarios'),
    path('funcionarios/cadastrar', funcionarios_cadastrar, name='funcionarios_cadastrar'),
    path('funcionarios/<int:id>/', funcionarios_editar, name='funcionarios_editar'),

    path('imoveis/', imoveis, name='imoveis'),
    path('imoveis/cadastrar', imoveis_cadastrar, name='imoveis_cadastrar'),
    path('imoveis/<int:id>', imoveis_editar, name='imoveis_editar'),

    path('clientes/', clientes, name='clientes'),
    path('clientes/cadastrar', clientes_cadastrar, name='clientes_cadastrar'),
    path('clientes/<int:id>/', clientes_editar, name='clientes_editar'),

    path('reservas/', reservas, name='reservas'),
    path('reservas/cadastrar', reservas_cadastrar, name='reservas_cadastrar'),
]