from django import forms
from .models import Imovel


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
