from django.urls import path
from .views import clientes

app_name = 'clientes'

urlpatterns = [
    path('<campo>/', clientes, name="lista"),
]
