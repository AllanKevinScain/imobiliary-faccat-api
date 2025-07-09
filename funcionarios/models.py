from django.db import models
import re


class Funcionario(models.Model):
    CARGO_CHOICES = [
        ('GER', 'Gerente'),
        ('ADM', 'Administrador'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20, blank=True)
    cargo = models.CharField(max_length=50, choices=CARGO_CHOICES)
    ativo = models.BooleanField(default=True)

    def formatar_nome(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome(self.nome)
        if self.telefone:
            self.telefone = re.sub(r'\D', '', self.telefone)
        super().save(*args, **kwargs)
