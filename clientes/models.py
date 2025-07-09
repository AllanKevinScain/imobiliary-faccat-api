from django.db import models
import re  # É uma biblioteca de expressões regualres do python


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    cpf = models.CharField(max_length=14, unique=True)
    data_nascimento = models.DateField(null=True, blank=True)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    def save(self, *args, **kwargs):
        if self.nome:
            self.nome = self.formatar_nome(self.nome)
        if self.telefone:
            self.telefone = self.formatar_telefone(self.telefone)
        if self.cpf:
            self.cpf = self.formatar_cpf(self.cpf)
        super().save(*args, **kwargs)

    def formatar_nome(self, nome):
        partes = nome.lower().split()
        minusculas = ['da', 'de', 'do', 'das', 'dos', 'e']

        return ' '.join([
            p if p in minusculas else p.capitalize()
            for p in partes
        ])

    def formatar_telefone(self, telefone):
        numeros = re.sub(r'\D', '', telefone)

        if len(numeros) == 11:
            return f"({numeros[:2]}) {numeros[2]} {numeros[3:7]}-{numeros[7:]}"
        return telefone

    def formatar_cpf(self, cpf):
        import re
        numeros = re.sub(r'\D', '', cpf)

        if len(numeros) == 11:
            return f"{numeros[:3]}.{numeros[3:6]}.{numeros[6:9]}-{numeros[9:]}"
        return cpf
