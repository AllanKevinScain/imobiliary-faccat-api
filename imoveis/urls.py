from django.urls import path
from .views import imoveis, cadastrar_imoveis, editar_imoveis, detalhes_imovel

app_name = 'imoveis'

urlpatterns = [
    path('editar/<id>', editar_imoveis, name='editar'),
    path('cadastrar/', cadastrar_imoveis, name='cadastrar'),
    path('<int:imovel_id>/', detalhes_imovel, name='detalhes'),
    path('<campo>/', imoveis, name="lista"),
]
