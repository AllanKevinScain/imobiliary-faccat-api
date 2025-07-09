from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'telefone'}))

    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'telefone']
