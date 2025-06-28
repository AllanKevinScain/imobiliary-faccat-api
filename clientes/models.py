from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
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
