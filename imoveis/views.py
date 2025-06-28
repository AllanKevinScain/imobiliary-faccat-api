from django.shortcuts import render
from .models import Imovel, Reserva
""" from .forms import ClienteForm """
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError

# IMOVEIS
ORDENACAO_IMOVEIS_LOOKUP = {
    'nome': 'nome',
    'tipo': 'tipo',
    'endereco': 'endereco',
    'cidade': 'cidade',
    'estado': 'estado',
    'disponivel': 'disponivel',
}


def imoveis(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        imoveis = Imovel.objects.filter(
            ativo=True, nome__icontains=query)
    else:
        imoveis = Imovel.objects.filter(ativo=True)
    if campo:
        campo_ordenacao = ORDENACAO_IMOVEIS_LOOKUP.get(campo)
        imoveis = imoveis.order_by(campo_ordenacao)
    dados = {'imoveis': imoveis, 'ativos': True}
    return render(request, 'imoveis/lista.html', dados)


def imoveis_inativos(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        imoveis = Imovel.objects.filter(
            ativo=False, nome__icontains=query)
    else:
        imoveis = Imovel.objects.filter(ativo=False)
    if campo:
        campo_ordenacao = ORDENACAO_IMOVEIS_LOOKUP.get(campo)
        imoveis = imoveis.order_by(campo_ordenacao)
    dados = {'imoveis': imoveis, 'ativos': False}
    return render(request, 'imoveis/lista.html', dados)


""" def imoveis_cadastrar(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('imoveis', campo='nome')
    else:
        form = ImovelForm()
    dados = {'form': form}
    return render(request, 'imoveis/imoveis_cadastrar.html', dados)


def imoveis_editar(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
    except:
        return redirect('imoveis', campo='nome')
    if request.method == 'POST':
        form = ImovelForm(request.POST, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('imoveis', campo='nome')
    form = ImovelForm(instance=imovel)
    dados = {'form': form, 'imovel': imovel}
    return render(request, 'imoveis/imoveis_editar.html', dados) """


def desativar_imovel(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
        imovel.ativo = False
        imovel.save()
        messages.success(request, "Imóvel desativar com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este imóvel, pois ele está vinculado a uma reserva.")
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")
    return redirect('imoveis:lista', campo='nome')


def ativar_imovel(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")
        return redirect('imoveis_inativos', campo='nome')
    if imovel.ativo == False:
        imovel.ativo = True
        imovel.save()
        messages.success(request, "Imóvel reativado com sucesso.")
    else:
        messages.info(request, "O imóvel já está ativo.")
    return redirect('imoveis_inativos', campo='nome')


# RESERVAS ----------------------------------------------------------------------------------------------------RESERVAS
ORDENACAO_RESERVAS_LOOKUP = {
    'imovel': 'imovel__nome',
    'cliente': 'cliente__nome',
    'funcionario': 'funcionario__nome',
    'data_inicio': 'data_inicio',
    'data_fim': 'data_fim',
}


def reservas(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'cliente' and query:
        reservas = Reserva.objects.filter(
            ativo=True, cliente__nome__icontains=query)
    else:
        reservas = Reserva.objects.filter(ativo=True)
    if campo:
        campo_ordenacao = ORDENACAO_RESERVAS_LOOKUP.get(campo)
        reservas = reservas.order_by(campo_ordenacao)
    dados = {'reservas': reservas, 'ativos': True}
    return render(request, 'reservas/lista.html', dados)


def reservas_inativas(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'cliente' and query:
        reservas = Reserva.objects.filter(
            ativo=False, cliente__nome__icontains=query)
    else:
        reservas = Reserva.objects.filter(ativo=False)
    if campo:
        campo_ordenacao = ORDENACAO_RESERVAS_LOOKUP.get(campo)
        reservas = reservas.order_by(campo_ordenacao)
    dados = {'reservas': reservas, 'ativos': False}
    return render(request, 'reservas/lista.html', dados)


""" def reservas_cadastrar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas', campo="cliente")
    else:
        form = ReservaForm()
    dados = {'form': form}
    return render(request, 'reservas/reservas_cadastrar.html', dados)


def reservas_editar(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
    except:
        return redirect('reservas', campo="cliente")
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('reservas', campo="cliente")
    form = ReservaForm(instance=reserva)
    dados = {'form': form, 'reserva': reserva}
    return render(request, 'reservas/reserva_editar.html', dados) """


def desativar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.ativo = False
        reserva.save()
        messages.success(request, "Reserva desativada com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar esta reserva, pois ela está vinculada a um imóvel ou cliente.")
    except Reserva.DoesNotExist:
        messages.error(request, "Reserva não encontrada.")
    return redirect('imoveis:lista_reservas', campo="cliente")


def ativar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
    except Reserva.DoesNotExist:
        messages.error(request, "Reserva não encontrada.")
        return redirect('reservas_inativas', campo="cliente")
    if reserva.ativo == False:
        reserva.ativo = True
        reserva.save()
        messages.success(request, "Reserva reativada com sucesso.")
    else:
        messages.info(request, "A reserva já está ativa.")
    return redirect('reservas_inativas', campo="cliente")
