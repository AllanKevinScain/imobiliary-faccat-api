from django import forms
from .models import Imovel, Reserva


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['foto', 'nome', 'tipo', 'endereco', 'qtyQuartos']
        labels = {
            'foto': 'Foto de perfil',
            'nome': 'Nome',
            'tipo': 'Tipo de locação',
            'endereco': 'Endereço',
            'qtyQuartos': 'Número de quartos',
        }


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
