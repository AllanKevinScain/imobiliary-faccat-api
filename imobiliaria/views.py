from django.shortcuts import render
from .models import Funcionario, Cliente, Imovel, Reserva
from .forms import FuncionarioForm, ClienteForm, ImovelForm, ReservaForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError


def index(request):
    return render(request, 'index.html')


# CLIENTES
ORDENACAO_CLIENTES_LOOKUP = {
    'nome': 'nome',
    'data_nascimento': 'data_nascimento',
}


def clientes(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        clientes = Cliente.objects.filter(ativo=True, nome__icontains=query)
    else:
        clientes = Cliente.objects.filter(ativo=True)
    if campo:
        campo_ordenacao = ORDENACAO_CLIENTES_LOOKUP.get(campo)
        clientes = clientes.order_by(campo_ordenacao)

    dados = {'clientes': clientes, 'ativos': True, 'query': query}
    return render(request, 'clientes/index.html', dados)


def clientes_inativos(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        clientes = Cliente.objects.filter(ativo=False, nome__icontains=query)
    else:
        clientes = Cliente.objects.filter(ativo=False)
    if campo:
        campo_ordenacao = ORDENACAO_CLIENTES_LOOKUP.get(campo)
        clientes = clientes.order_by(campo_ordenacao)

    dados = {'clientes': clientes, 'ativos': False, 'query': query}
    return render(request, 'clientes/index.html', dados)


def clientes_cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes', campo="nome")
    else:
        form = ClienteForm()
    dados = {'form': form}
    return render(request, 'clientes/clientes_cadastrar.html', dados)


def clientes_editar(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except:
        return redirect('clientes', campo="nome")
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes', campo="nome")
    form = ClienteForm(instance=cliente)
    dados = {'form': form, 'cliente': cliente}
    return render(request, 'clientes/clientes_editar.html', dados)


def desativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.ativo = False
        cliente.save()
        messages.success(request, "Cliente desativado com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este cliente, pois ele está vinculado a uma reserva.")
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
    return redirect('clientes', campo="nome")


def ativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect('clientes_inativos', campo="nome")
    if cliente.ativo == False:
        cliente.ativo = True
        cliente.save()
        messages.success(request, "Cliente reativado com sucesso.")
    else:
        messages.info(request, "O cliente já está ativo.")
    return redirect('clientes_inativos', campo="nome")


# FUNCIONARIOS ------------------------------------------------------------------
ORDENACAO_FUNCIONARIO_LOOKUP = {
    'nome': 'nome',
    'cargo': 'cargo',
}


def funcionarios(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        funcionarios = Funcionario.objects.filter(
            ativo=True, nome__icontains=query)
    else:
        funcionarios = Funcionario.objects.filter(ativo=True)
    if campo:
        campo_ordenacao = ORDENACAO_FUNCIONARIO_LOOKUP.get(campo)
        funcionarios = funcionarios.order_by(campo_ordenacao)
    dados = {'funcionarios': funcionarios, 'ativos': True, 'query': query}
    return render(request, 'funcionarios/index.html', dados)


def funcionarios_inativos(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        funcionarios = Funcionario.objects.filter(
            ativo=False, nome__icontains=query)
    else:
        funcionarios = Funcionario.objects.filter(ativo=False)
    if campo:
        campo_ordenacao = ORDENACAO_FUNCIONARIO_LOOKUP.get(campo)
        funcionarios = funcionarios.order_by(campo_ordenacao)
    dados = {'funcionarios': funcionarios, 'ativos': False, 'query': query}
    return render(request, 'funcionarios/index.html', dados)


def funcionarios_cadastrar(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios', campo='nome')
    else:
        form = FuncionarioForm()

    dados = {'form': form}
    return render(request, 'funcionarios/funcionarios_cadastrar.html', dados)


def funcionarios_editar(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except:
        return redirect('funcionarios', campo='nome')
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios', campo='nome')
    form = FuncionarioForm(instance=funcionario)
    dados = {'form': form, 'funcionario': funcionario}
    return render(request, 'funcionarios/funcionarios_editar.html', dados)


def desativar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
        funcionario.ativo = False
        funcionario.save()
        messages.success(request, "Funcionário desativado com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este funcionário, pois ele está vinculado a uma reserva.")
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")
    return redirect('funcionarios', campo='nome')


def ativar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")
        return redirect('funcionarios_inativos', campo='nome')
    if funcionario.ativo == False:
        funcionario.ativo = True
        funcionario.save()
        messages.success(request, "Funcionario reativado com sucesso.")
    else:
        messages.info(request, "O funcionário já está ativo.")
    return redirect('funcionarios_inativos', campo='nome')


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
    return render(request, 'imoveis/index.html', dados)


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
    return render(request, 'imoveis/index.html', dados)


def imoveis_cadastrar(request):
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
    return render(request, 'imoveis/imoveis_editar.html', dados)


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
    return redirect('imoveis', campo='nome')


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


# RESERVAS
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
    return render(request, 'reservas/index.html', dados)


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
    return render(request, 'reservas/index.html', dados)


def reservas_cadastrar(request):
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
    return render(request, 'reservas/reserva_editar.html', dados)


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
    return redirect('reservas', campo="cliente")


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
