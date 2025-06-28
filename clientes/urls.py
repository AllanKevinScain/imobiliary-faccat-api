from django.urls import path
from .views import clientes, clientes_cadastrar, editar_clientes

app_name = 'clientes'

urlpatterns = [
    path('editar/<id>/', editar_clientes, name='editar'),
    path('cadastrar/', clientes_cadastrar, name='cadastrar'),
    path('<campo>/', clientes, name="lista"),
]
