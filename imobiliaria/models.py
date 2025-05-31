from django.db import models

class Funcionario(models.Model):
    CARGO_CHOICES = [
        ('GER', 'Gerente'),
        ('VEN', 'Vendedor'),
        ('ADM', 'Administrador'),
        ('SUP', 'Supervisor'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Imovel(models.Model):
    TIPO_CHOICES = [
        ('AP', 'Apartamento'),
        ('CA', 'Casa'),
        ('SC', 'Sala Comercial'),
    ]

    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_CHOICES)
    endereco = models.CharField(max_length=255)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

class Quarto(models.Model):
    imovel = models.ForeignKey(Imovel, related_name='quartos', on_delete=models.RESTRICT)
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Reserva(models.Model):
    imovel = models.ForeignKey(Imovel, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.SET_NULL, null=True)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    def __str__(self):
        return f"Reserva de {self.imovel} para {self.cliente}"

    class Meta:
        unique_together = ('imovel', 'data_inicio', 'data_fim')