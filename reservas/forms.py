from django import forms
from django.core.exceptions import ValidationError
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

    def clean(self):
        cleaned_data = super().clean()
        imovel = cleaned_data.get('imovel')
        data_inicio = cleaned_data.get('data_inicio')
        data_fim = cleaned_data.get('data_fim')

        if imovel and data_inicio and data_fim:
            conflitos = Reserva.objects.filter(
                imovel=imovel,
                data_inicio=data_inicio,
                data_fim=data_fim,
                ativo=True
            )

            # Se estiver editando uma reserva existente, exclui ela mesma da verificação
            if self.instance.pk:
                conflitos = conflitos.exclude(pk=self.instance.pk)

            if conflitos.exists():
                raise ValidationError(
                    "Já existe uma reserva ativa para este imóvel neste período.")

        return cleaned_data
