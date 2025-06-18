from django.urls import path

from .views import index, funcionarios_cadastrar, funcionarios_editar, desativar_funcionario, ativar_funcionario, funcionarios, funcionarios_inativos
from .views import imoveis, imoveis_cadastrar, imoveis_editar, desativar_imovel, ativar_imovel, imoveis_inativos
from .views import clientes, clientes_cadastrar, clientes_editar, desativar_cliente, ativar_cliente, clientes_inativos
from .views import reservas, reservas_cadastrar, reservas_editar, desativar_reserva, ativar_reserva, reservas_inativas

urlpatterns = [
    path('', index, name='index'),
    # ------------------------------------------------------------------------------------------
    # listagem funcionários
    path('funcionarios/<campo>/', funcionarios, name='funcionarios'),
    path('funcionarios/inativos/<campo>/', funcionarios_inativos,
         name='funcionarios_inativos'),


    # crud funcionários
    path('funcionarios/cadastrar', funcionarios_cadastrar,
         name='funcionarios_cadastrar'),
    path('funcionarios/<int:id>/', funcionarios_editar,
         name='funcionarios_editar'),
    path('funcionarios/ativar/<int:id>/',
         ativar_funcionario, name='ativar_funcionario'),
    path('funcionarios/<int:id>/desativar/',
         desativar_funcionario, name='desativar_funcionario'),
    # ------------------------------------------------------------------------------------------
    # listagem imóveis
    path('imoveis/<campo>/', imoveis, name='imoveis'),
    path('imoveis/inativos/<campo>/', imoveis_inativos, name='imoveis_inativos'),

    # crud imóveis
    path('imoveis/cadastrar', imoveis_cadastrar, name='imoveis_cadastrar'),
    path('imoveis/<int:id>', imoveis_editar, name='imoveis_editar'),
    path('imoveis/ativar/<int:id>/', ativar_imovel, name='ativar_imovel'),
    path('imoveis/<int:id>/desativar/',
         desativar_imovel, name='desativar_imovel'),
    # ------------------------------------------------------------------------------------------
    # listagem clientes
    path('clientes/<campo>/', clientes, name='clientes'),
    path('clientes/inativos/<campo>/',
         clientes_inativos, name='clientes_inativos'),

    # crud clientes
    path('clientes/cadastrar', clientes_cadastrar, name='clientes_cadastrar'),
    path('clientes/<int:id>/', clientes_editar, name='clientes_editar'),
    path('clientes/ativar/<int:id>/', ativar_cliente, name='ativar_cliente'),
    path('clientes/<int:id>/desativar/',
         desativar_cliente, name='desativar_cliente'),
    # ------------------------------------------------------------------------------------------
    # listagem reservas
    path('reservas/<campo>/', reservas, name='reservas'),
    path('reservas/inativas/<campo>/',
         reservas_inativas, name='reservas_inativas'),

    # crud reservas
    path('reservas/cadastrar', reservas_cadastrar, name='reservas_cadastrar'),
    path('reservas/<int:id>/', reservas_editar, name='reservas_editar'),
    path('reservas/ativar/<int:id>/', ativar_reserva, name='ativar_reserva'),
    path('reservas/<int:id>/desativar/',
         desativar_reserva, name='desativar_reserva'),
]
