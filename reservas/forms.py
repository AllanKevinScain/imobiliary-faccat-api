from django import forms
from .models import Reserva
from imoveis.models import Imovel


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['imovel', 'cliente', 'data_inicio', 'data_fim']
        widgets = {
            'data_inicio': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'data_fim': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imovel'].queryset = Imovel.objects.filter(
            disponibilidade=True, ativo=True)
