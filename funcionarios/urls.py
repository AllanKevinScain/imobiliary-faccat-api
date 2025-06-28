from django.urls import path
from .views import funcionarios, cadastrar_funcionarios

app_name = 'funcionarios'

urlpatterns = [
    path('cadastrar/', cadastrar_funcionarios, name='cadastrar'),
    path('<campo>/', funcionarios, name="lista"),
]
