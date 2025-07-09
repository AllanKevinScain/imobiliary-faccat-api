from django.shortcuts import render
from .models import Reserva
from .forms import ReservaForm
from historico_locacoes.models import HistoricoAcao
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

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

            return redirect('reservas:lista', campo="cliente")
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

    return redirect('reservas:lista', campo="cliente")


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

    return redirect('reservas:lista', campo="cliente")
