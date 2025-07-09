from django.shortcuts import render
from .models import Imovel, Reserva
from .forms import ImovelForm, ReservaForm
from historico_locacoes.models import HistoricoAcao
from django.shortcuts import get_object_or_404, redirect
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
    dados = {'imoveis': imoveis, 'ativos': True}
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
        messages.success(request, "Imóvel desativado com sucesso.")
        imovel.save()
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este imóvel, pois ele está vinculado a uma reserva.")
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

    dados = {
        'imovel': imovel,
    }

    return render(request, 'imoveis/detalhes.html', dados)


# RESERVAS ----------------------------------------------------------------------------------------------------RESERVAS
ORDENACAO_RESERVAS_LOOKUP = {
    'imovel': 'imovel__nome',
    'cliente': 'cliente__nome',
    'funcionario': 'funcionario__nome',
    'data_inicio': 'data_inicio',
    'data_fim': 'data_fim',
}


@login_required
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


@login_required
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


@login_required
def cadastrar_reservas(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)

            imovel = reserva.imovel
            imovel.disponibilidade = False
            imovel.save()
            reserva.save()

            HistoricoAcao.objects.create(
                usuario=request.user,
                imovel=imovel,
                reserva=reserva,
                acao='RESERVAR',
                descricao=f"Reserva de {imovel.nome} para {reserva.cliente}"
            )

            return redirect('imoveis:lista_reservas', campo="cliente")
    else:
        form = ReservaForm()
    dados = {'form': form}
    return render(request, 'reservas/cadastrar.html', dados)


@login_required
def cancelar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if reserva.ativo:
        reserva.ativo = False
        reserva.save()

        imovel = reserva.imovel
        imovel.disponibilidade = True
        imovel.save()

        HistoricoAcao.objects.create(
            usuario=request.user,
            imovel=imovel,
            reserva=reserva,
            acao='CANCELAR',
            descricao=f"Reserva de {imovel.nome} para {reserva.cliente} foi cancelada."
        )

    return redirect('imoveis:lista_reservas', campo="cliente")


@login_required
def finalizar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)

    if reserva.ativo:
        reserva.ativo = False
        reserva.save()

        imovel = reserva.imovel
        imovel.disponibilidade = True
        imovel.save()

        HistoricoAcao.objects.create(
            usuario=request.user,
            imovel=imovel,
            reserva=reserva,
            acao='FINALIZAR',
            descricao=f"Reserva de {imovel.nome} para {reserva.cliente} foi finalizada."
        )

    return redirect('imoveis:lista_reservas', campo="cliente")
