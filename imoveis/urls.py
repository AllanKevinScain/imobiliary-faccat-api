from django.urls import path
from .views import imoveis, reservas

app_name = 'imoveis'

urlpatterns = [
    path('<campo>/', imoveis, name="lista"),
    path('reservas/<campo>/', reservas, name='lista_reservas'),
]
