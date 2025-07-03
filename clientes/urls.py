from django.urls import path
from .views import clientes, clientes_cadastrar, editar_clientes, clientes_inativos, desativar_cliente, ativar_cliente

app_name = 'clientes'

urlpatterns = [
    path('editar/<id>/', editar_clientes, name='editar'),
    path('cadastrar/', clientes_cadastrar, name='cadastrar'),
    path('inativos/<campo>/', clientes_inativos, name="lista_inativos"),
    path('desativar/<id>/', desativar_cliente, name='desativar'),
    path('ativar/<id>/', ativar_cliente, name='ativar'),
    path('<campo>/', clientes, name="lista"),
]
