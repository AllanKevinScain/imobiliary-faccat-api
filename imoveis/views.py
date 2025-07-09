from django.shortcuts import render
from .models import Imovel
from .forms import ImovelForm, FiltroImovelForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError
from django.contrib.auth.decorators import login_required

# IMOVEIS
ORDENACAO_IMOVEIS_LOOKUP = {
    'foto': 'foto',
    'nome': 'nome',
    'tipo': 'tipo',
    'endereco': 'endereco',
}


@login_required
def imoveis(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        imoveis = Imovel.objects.filter(nome__icontains=query)
    else:
        imoveis = Imovel.objects.filter()
    if campo:
        campo_ordenacao = ORDENACAO_IMOVEIS_LOOKUP.get(campo)
        imoveis = imoveis.order_by(campo_ordenacao)
    dados = {'imoveis': imoveis, 'ativos': True, 'query': query}
    return render(request, 'imoveis/lista.html', dados)


@login_required
def cadastrar_imoveis(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('imoveis:lista', campo='nome')
    else:
        form = ImovelForm()
    dados = {'form': form}
    return render(request, 'imoveis/cadastrar.html', dados)


@login_required
def editar_imoveis(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
    except:
        return redirect('imoveis:lista', campo='nome')
    if request.method == 'POST':
        form = ImovelForm(request.POST, instance=imovel, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Informações salvas com sucesso.")

            return redirect('imoveis:lista', campo='nome')
    form = ImovelForm(instance=imovel)
    dados = {'form': form, 'imovel': imovel}
    return render(request, 'imoveis/editar.html', dados)


@login_required
def desativar_imovel(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
        imovel.ativo = False
        messages.success(request, "Imóvel desativado com sucesso.")
        imovel.save()
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este imóvel, pois ele está vinculado a uma reserva.")
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")
    return redirect('imoveis:lista', campo='nome')


@login_required
def ativar_imovel(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
        imovel.ativo = True
        messages.success(request, "Imóvel ativado com sucesso.")
        imovel.save()
    except RestrictedError:
        messages.error(
            request, "Não é possível ativado este imóvel, pois ele está vinculado a uma reserva.")
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")
    return redirect('imoveis:lista', campo='nome')


@login_required
def detalhes_imovel(request, imovel_id):
    try:
        imovel = Imovel.objects.get(id=imovel_id)
    except Imovel.DoesNotExist:
        messages.error(request, "Imovel não encontrado.")
        return redirect('imoveis:lista', campo='nome')
    dados = {'imovel': imovel}
    return render(request, 'imoveis/detalhes.html', dados)


@login_required
def filtrar_imoveis(request):
    form = FiltroImovelForm(request.GET or None)
    imoveis = Imovel.objects.all()

    if form.is_valid():
        nome = form.cleaned_data.get('nome')
        endereco = form.cleaned_data.get('endereco')
        preco = form.cleaned_data.get('preco')
        disponibilidade = form.cleaned_data.get('disponibilidade')
        quartos_min = form.cleaned_data.get('quartos_min')
        quartos_max = form.cleaned_data.get('quartos_max')

        if nome:
            imoveis = imoveis.filter(nome__icontains=nome)
        if endereco:
            imoveis = imoveis.filter(endereco__icontains=endereco)
        if preco:
            imoveis = imoveis.filter(preco__icontains=preco)
        if disponibilidade == 'disponivel':
            imoveis = imoveis.filter(disponibilidade=True)
        elif disponibilidade == 'indisponivel':
            imoveis = imoveis.filter(disponibilidade=False)
        if quartos_min is not None:
            imoveis = imoveis.filter(qtyQuartos__gte=quartos_min)
        if quartos_max is not None:
            imoveis = imoveis.filter(qtyQuartos__lte=quartos_max)

    return render(request, 'imoveis/filtro.html', {
        'form': form,
        'imoveis': imoveis
    })
