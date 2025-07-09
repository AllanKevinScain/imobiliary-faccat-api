from django.urls import path
from .views import reservas, cadastrar_reservas, cancelar_reserva, finalizar_reserva, reservas_inativas
from .views import imoveis, cadastrar_imoveis, editar_imoveis, detalhes_imovel, desativar_imovel, ativar_imovel

app_name = 'imoveis'

urlpatterns = [
    # reservas
    path('reservas/cadastrar/', cadastrar_reservas, name='cadastrar_reserva'),
    path('reservas/cancelar/<id>', cancelar_reserva, name='cancelar'),
    path('reservas/finalizar/<id>', finalizar_reserva, name='finalizar'),
    path('reservas/indisponibilizar/<id>',
         desativar_imovel, name='indisponibilizar'),
    path('reservas/disponibilizar/<id>', ativar_imovel, name='disponibilizar'),


    path('reservas/encerrados/<campo>/', reservas_inativas,
         name='lista_reservas_encerrados'),
    path('reservas/<campo>/', reservas, name='lista_reservas'),

    # imóveis
    path('editar/<id>', editar_imoveis, name='editar'),
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),

    path('<int:imovel_id>/', detalhes_imovel, name='detalhes_imovel'),
    path('<campo>/', imoveis, name="lista"),
]
