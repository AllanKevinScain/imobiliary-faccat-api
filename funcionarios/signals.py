from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Funcionario
import re


@receiver(post_save, sender=Funcionario)
def criar_usuario_para_funcionario(sender, instance, created, **kwargs):
    if created and not instance.user:
        nome = instance.nome.replace(" ", "").lower()
        telefone = re.sub(r'\D', '', instance.telefone or "")
        ultimos_digitos = telefone[-3:] if len(telefone) >= 3 else "000"
        senha = f"funcionario{ultimos_digitos}"

        username_base = nome
        count = 1
        while User.objects.filter(username=nome).exists():
            nome = f"{username_base}{count}"
            count += 1

        user = User.objects.create_user(
            username=nome,
            email=instance.email,
            password=senha,
            first_name=instance.nome
        )
        instance.user = user
        instance.save()
