from django.db import models
from imoveis.models import Imovel


class Ocorrencia(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_ocorrencia = models.DateField(auto_now_add=True)
    enviado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.titulo} - {self.imovel.nome}"
