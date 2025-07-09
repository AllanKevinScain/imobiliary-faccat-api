from django.urls import path
from .views import listar_historico

app_name = 'historico_locacoes'

urlpatterns = [
    path('', listar_historico, name='lista'),
]
