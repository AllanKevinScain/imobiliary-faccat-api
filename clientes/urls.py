from django.urls import path
from .views import clientes, clientes_cadastrar

app_name = 'clientes'

urlpatterns = [
    path('cadastrar/', clientes_cadastrar, name='cadastrar'),
    path('<campo>/', clientes, name="lista"),
]
