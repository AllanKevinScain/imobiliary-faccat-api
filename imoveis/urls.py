from django.urls import path
from .views import reservas, cadastrar_reservas
from .views import quartos, cadastrar_quarto
from .views import imoveis, cadastrar_imoveis, editar_imoveis

app_name = 'imoveis'

urlpatterns = [
    # quartos
    path('quartos/<imovel_id>/', quartos, name='lista_quartos'),
    path('quartos/<imovel_id>/cadastrar/',
         cadastrar_quarto, name='cadastrar_quarto'),

    # reservas
    path('reservas/cadastrar/', cadastrar_reservas, name='cadastrar_reserva'),
    path('reservas/<campo>/', reservas, name='lista_reservas'),

    # imóveis
    path('editar/<id>', editar_imoveis, name='editar'),
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),
    path('<campo>/', imoveis, name="lista"),
]
