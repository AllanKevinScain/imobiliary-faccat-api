from django import forms


class HistoricoFiltroForm(forms.Form):
    tipo = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Todos'),
            ('AP', 'Apartamento'),
            ('CA', 'Casa'),
            ('SC', 'Sala Comercial'),
        ]
    )
    acao = forms.ChoiceField(
        required=False,
        choices=[
            ('', 'Todas'),
            ('RESERVAR', 'Reservou imóvel'),
            ('FINALIZAR', 'Finalizou reserva'),
            ('CANCELAR', 'Cancelou reserva'),
        ]
    )
    data_inicio = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    data_fim = forms.DateField(
        required=False, widget=forms.DateInput(attrs={'type': 'date'}))
