from django import forms
from .models import Ocorrencia


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = ['imovel', 'titulo', 'descricao']
