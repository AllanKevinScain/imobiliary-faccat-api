from django.urls import path
from .views import imoveis, cadastrar_imoveis, editar_imoveis, detalhes_imovel, filtrar_imoveis

app_name = 'imoveis'

urlpatterns = [
    path('editar/<id>', editar_imoveis, name='editar'),
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),
    path('filtro', filtrar_imoveis, name='lista_filtro'),
    path('<int:imovel_id>/', detalhes_imovel, name='detalhes'),
    path('<campo>/', imoveis, name="lista"),
]
