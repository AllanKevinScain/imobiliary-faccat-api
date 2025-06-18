from django import forms
from .models import Funcionario, Cliente, Imovel, Quarto, Reserva

# Formulário para Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'email', 'telefone', 'cargo']

# Formulário para Cliente


class ClienteForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        input_formats=['%Y-%m-%d']
    )

    class Meta:
        model = Cliente
        fields = ['nome', 'email', 'telefone', 'cpf', 'data_nascimento']

# Formulário para Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['nome', 'tipo', 'endereco', 'cidade', 'estado', 'disponivel']

# Formulário para Quarto


class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['imovel', 'nome']

# Formulário para Reserva


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['imovel', 'cliente',
                  'funcionario', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'data_fim': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
        input_formats = ['%Y-%m-%d']
