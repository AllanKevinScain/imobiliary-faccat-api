from django.db import models
from clientes.models import Cliente
from funcionarios.models import Funcionario


class Imovel(models.Model):
    TIPO_CHOICES = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('SC', 'Sala Comercial'),
    ]

    ESTADO_CHOICES = [
        # ('AC', 'Acre'),
        # ('AL', 'Alagoas'),
        # ('AP', 'Amapá'),
        # ('AM', 'Amazonas'),
        # ('BA', 'Bahia'),
        # ('CE', 'Ceará'),
        # ('DF', 'Distrito Federal'),
        # ('ES', 'Espírito Santo'),
        # ('GO', 'Goiás'),
        # ('MA', 'Maranhão'),
        # ('MT', 'Mato Grosso'),
        # ('MS', 'Mato Grosso do Sul'),
        # ('MG', 'Minas Gerais'),
        # ('PA', 'Pará'),
        # ('PB', 'Paraíba'),
        # ('PR', 'Paraná'),
        # ('PE', 'Pernambuco'),
        # ('PI', 'Piauí'),
        # ('RJ', 'Rio de Janeiro'),
        # ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        # ('RO', 'Rondônia'),
        # ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        # ('SE', 'Sergipe'),
        # ('TO', 'Tocantins'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
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


class Quarto(models.Model):
    imovel = models.ForeignKey(
        Imovel, related_name='quartos', on_delete=models.RESTRICT)
    nome = models.CharField(max_length=50)
    disponibilidade = models.BooleanField(default=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome


class Reserva(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.RESTRICT)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    funcionario = models.ForeignKey(
        Funcionario, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f"Reserva de {self.imovel} para {self.cliente}"

    class Meta:
        unique_together = ('imovel', 'data_inicio', 'data_fim')
