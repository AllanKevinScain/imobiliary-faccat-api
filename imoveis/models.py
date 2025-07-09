from stdimage.models import StdImageField
from django.db import models
from clientes.models import Cliente


class Imovel(models.Model):
    TIPO_CHOICES = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('SC', 'Sala Comercial'),
    ]

    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)

    qtyQuartos = models.IntegerField()
    foto = StdImageField(
        upload_to='fotos/imoveis',
        variations={'thumb': (150, 150), 'medium': (300, 300)},
        blank=True,
        null=True
    )

    disponibilidade = models.BooleanField(default=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome(self.nome)
        super().save(*args, **kwargs)

    def formatar_nome(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])


class Reserva(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Reserva de {self.imovel} ({self.imovel.imovel}) para {self.cliente}"

    class Meta:
        unique_together = ('imovel', 'data_inicio', 'data_fim')
