from django.urls import path
from .views import reservas
from .views import quartos, cadastrar_quarto
from .views import imoveis, cadastrar_imoveis

app_name = 'imoveis'

urlpatterns = [
    # quartos
    path('quartos/<imovel_id>/', quartos, name='lista_quartos'),
    path('quartos/<imovel_id>/cadastrar/',
         cadastrar_quarto, name='cadastrar_quarto'),

    # reservas
    path('reservas/<campo>/', reservas, name='lista_reservas'),

    # imóveis
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),
    path('<campo>/', imoveis, name="lista"),
]
