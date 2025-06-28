from django.urls import path
from .views import funcionarios, cadastrar_funcionarios, editar_funcionarios

app_name = 'funcionarios'

urlpatterns = [
    path('editar/<id>', editar_funcionarios, name='editar'),
    path('cadastrar/', cadastrar_funcionarios, name='cadastrar'),
    path('<campo>/', funcionarios, name="lista"),
]
