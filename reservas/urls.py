from django.urls import path
from .views import reservas, cadastrar_reservas, cancelar_reserva, finalizar_reserva, reservas_inativas
from imoveis.views import desativar_imovel, ativar_imovel

app_name = 'reservas'

urlpatterns = [
    path('cadastrar/', cadastrar_reservas, name='cadastrar'),
    path('cancelar/<id>', cancelar_reserva, name='cancelar'),
    path('finalizar/<id>', finalizar_reserva, name='finalizar'),
    path('indisponibilizar/<id>', desativar_imovel, name='indisponibilizar'),
    path('disponibilizar/<id>', ativar_imovel, name='disponibilizar'),
    path('encerrados/<campo>/', reservas_inativas, name='lista_encerrados'),
    path('<campo>/', reservas, name='lista'),
]
