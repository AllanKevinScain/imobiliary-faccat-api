from django.db import models
from clientes.models import Cliente
from imoveis.models import Imovel


class Reserva(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Reserva de {self.imovel} ({self.imovel.imovel}) para {self.cliente}"
