from stdimage.models import StdImageField
from django.db import models


class Imovel(models.Model):
    TIPO_CHOICES = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('SC', 'Sala Comercial'),
    ]

    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)

    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

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
