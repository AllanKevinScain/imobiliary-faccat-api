from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import HistoricoAcao
from .forms import HistoricoFiltroForm
from django.utils.dateparse import parse_date


@login_required
def listar_historico(request):
    form = HistoricoFiltroForm(request.GET or None)
    historico = HistoricoAcao.objects.all().select_related(
        'usuario', 'imovel', 'reserva').order_by('-data')

    if form.is_valid():
        cd = form.cleaned_data
        if cd.get('busca'):
            historico = historico.filter(imovel__nome__icontains=cd['busca'])
        if cd.get('tipo'):
            historico = historico.filter(imovel__tipo=cd['tipo'])
        if cd.get('acao'):
            historico = historico.filter(acao=cd['acao'])
        if cd.get('data_inicio'):
            historico = historico.filter(data__date__gte=cd['data_inicio'])
        if cd.get('data_fim'):
            historico = historico.filter(data__date__lte=cd['data_fim'])

    return render(request, 'historico/lista.html', {'form': form, 'historico': historico})
