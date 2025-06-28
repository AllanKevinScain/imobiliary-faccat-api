from django.urls import path
from .views import funcionarios

app_name = 'funcionarios'

urlpatterns = [
    path('<campo>/', funcionarios, name="lista"),
]
