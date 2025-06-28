from django import forms
from .models import Imovel, Quarto, Reserva


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['nome', 'tipo', 'endereco', 'cidade', 'estado']


class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = ['nome']


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['quarto', 'cliente', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'data_fim': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }
