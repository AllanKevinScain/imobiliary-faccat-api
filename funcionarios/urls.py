from django.urls import path
from .views import funcionarios, cadastrar_funcionarios, editar_funcionarios, funcionarios_inativos, desativar_funcionario, ativar_funcionario

app_name = 'funcionarios'

urlpatterns = [
    path('editar/<id>', editar_funcionarios, name='editar'),
    path('cadastrar/', cadastrar_funcionarios, name='cadastrar'),
    path('inativos/<campo>/', funcionarios_inativos, name="lista_inativos"),
    path('desativar/<id>/', desativar_funcionario, name="desativar"),
    path('ativar/<id>/', ativar_funcionario, name="ativar"),
    path('<campo>/', funcionarios, name="lista"),
]
