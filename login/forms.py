from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UsuarioCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        labels = {
            'username': 'Usuário',
            'first_name': 'Nome',
            'email': 'E-mail',
            'password1': 'Senha',
            'password2': 'Confirmação de Senha',
        }
