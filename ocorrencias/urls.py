from django.urls import path
from .views import registrar_ocorrencia

app_name = 'ocorrencias'

urlpatterns = [
    path('', registrar_ocorrencia, name='registrar'),
]
