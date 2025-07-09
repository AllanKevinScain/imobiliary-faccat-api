from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )
    telefone = forms.CharField(
        widget=forms.TextInput(attrs={'id': 'telefone'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'id': 'cpf'}))

    class Meta:
        model = Cliente
        fields = ['nome', 'telefone', 'cpf', 'data_nascimento']
