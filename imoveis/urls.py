from django.urls import path
from .views import reservas
from .views import imoveis, cadastrar_imoveis

app_name = 'imoveis'

urlpatterns = [
    path('reservas/<campo>/', reservas, name='lista_reservas'),

    # imóveis
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),
    path('<campo>/', imoveis, name="lista"),
]
