from django.urls import path

from .views import index, funcionarios, funcionarios_cadastrar, funcionarios_editar, desativar_funcionario, ativar_funcionario
from .views import imoveis, imoveis_cadastrar, imoveis_editar, desativar_imovel, ativar_imovel
from .views import clientes, clientes_cadastrar, clientes_editar, desativar_cliente, ativar_cliente
from .views import reservas, reservas_cadastrar, reservas_editar, desativar_reserva, ativar_reserva

urlpatterns = [
    path('', index, name='index'),

    path('funcionarios/', funcionarios, name='funcionarios'),
    path('funcionarios/cadastrar', funcionarios_cadastrar,
         name='funcionarios_cadastrar'),
    path('funcionarios/<int:id>/', funcionarios_editar,
         name='funcionarios_editar'),
    path('funcionarios/inativos/', funcionarios, name='funcionarios_inativos'),
    path('funcionarios/ativar/<int:id>/', ativar_funcionario,
         name='ativar_funcionario'),
    path('funcionarios/<int:id>/desativar/',
         desativar_funcionario, name='desativar_funcionario'),

    path('imoveis/', imoveis, name='imoveis'),
    path('imoveis/cadastrar', imoveis_cadastrar, name='imoveis_cadastrar'),
    path('imoveis/<int:id>', imoveis_editar, name='imoveis_editar'),
    path('imoveis/inativos/', imoveis, name='imoveis_inativos'),
    path('imoveis/ativar/<int:id>/', ativar_imovel, name='ativar_imovel'),
    path('imoveis/<int:id>/desativar/',
         desativar_imovel, name='desativar_imovel'),

    path('clientes/', clientes, name='clientes'),
    path('clientes/cadastrar', clientes_cadastrar, name='clientes_cadastrar'),
    path('clientes/<int:id>/', clientes_editar, name='clientes_editar'),
    path('clientes/inativos/', clientes, name='clientes_inativos'),
    path('clientes/ativar/<int:id>/', ativar_cliente, name='ativar_cliente'),
    path('clientes/<int:id>/desativar/',
         desativar_cliente, name='desativar_cliente'),

    path('reservas/', reservas, name='reservas'),
    path('reservas/cadastrar', reservas_cadastrar, name='reservas_cadastrar'),
    path('reservas/<int:id>/', reservas_editar, name='reservas_editar'),
    path('reservas/inativas/', reservas, name='reservas_inativas'),
    path('reservas/ativar/<int:id>/', ativar_reserva, name='ativar_reserva'),
    path('reservas/<int:id>/desativar/',
         desativar_reserva, name='desativar_reserva'),
]
