from django.db import models
from django.contrib.auth.models import User
from imoveis.models import Imovel
from reservas.models import Reserva


class HistoricoAcao(models.Model):
    ACOES_CHOICES = [
        ('CRIAR_IMOVEL', 'Criou imóvel'),
        ('EDITAR_IMOVEL', 'Editou imóvel'),
        ('RESERVAR', 'Reservou imóvel'),
        ('FINALIZAR', 'Finalizou reserva'),
        ('CANCELAR', 'Cancelou reserva'),
    ]
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    imovel = models.ForeignKey(
        Imovel, on_delete=models.SET_NULL, null=True, blank=True)
    reserva = models.ForeignKey(
        Reserva, on_delete=models.SET_NULL, null=True, blank=True)
    acao = models.CharField(max_length=20, choices=ACOES_CHOICES)
    descricao = models.TextField(blank=True)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario} - {self.get_acao_display()} em {self.data.strftime('%d/%m/%Y %H:%M')}"
