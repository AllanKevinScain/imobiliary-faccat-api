from django.urls import path
from .views import reservas, cadastrar_reservas, reserva_quarto
from .views import quartos, cadastrar_quarto, editar_quartos
from .views import imoveis, cadastrar_imoveis, editar_imoveis

app_name = 'imoveis'

urlpatterns = [
    # quartos
    path('quartos/<id>/editar/', editar_quartos, name='editar_quarto'),
    path('quartos/<imovel_id>/cadastrar/',
         cadastrar_quarto, name='cadastrar_quarto'),
    path('quartos/<imovel_id>/', quartos, name='lista_quartos'),

    # reservas
    path('reservas/cadastrar/', cadastrar_reservas, name='cadastrar_reserva'),
    path('reservas/id/<reserva_id>/', reserva_quarto, name='reserva_quarto'),
    path('reservas/<campo>/', reservas, name='lista_reservas'),

    # imóveis
    path('editar/<id>', editar_imoveis, name='editar'),
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),
    path('<campo>/', imoveis, name="lista"),
]
