from django import forms
from .models import Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = ['foto', 'nome', 'tipo', 'endereco', 'qtyQuartos']
        labels = {
            'foto': 'Foto de perfil',
            'nome': 'Nome da locação',
            'tipo': 'Tipo de locação',
            'endereco': 'Endereço',
            'qtyQuartos': 'Número de quartos',
        }


class FiltroImovelForm(forms.Form):
    nome = forms.CharField(label='Nome', required=False)
    endereco = forms.CharField(label='Endereço', required=False)
    disponibilidade = forms.ChoiceField(
        label='Disponibilidade',
        required=False,
        choices=[
            ('', 'Todos'),
            ('disponivel', 'Disponível'),
            ('indisponivel', 'Indisponível'),
        ]
    )
    quartos_min = forms.IntegerField(label='Mínimo de Quartos', required=False)
    quartos_max = forms.IntegerField(label='Máximo de Quartos', required=False)
