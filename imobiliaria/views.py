from django.shortcuts import render
from .models import Funcionario, Cliente, Imovel, Quarto, Reserva
from .forms import FuncionarioForm, ClienteForm, ImovelForm, QuartoForm, ReservaForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError

# Create your views here.


def index(request):
    return render(request, 'index.html')

# FUNCIONARIOS


def funcionarios(request):
    funcionarios = Funcionario.objects.filter(ativo=True)

    dados = {
        'funcionarios': funcionarios,
        'ativos': True,  # Para indicar que estamos mostrando funcionários ativos
    }

    return render(request, 'funcionarios/index.html', dados)


def funcionarios_cadastrar(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')
    else:
        # form vai receber um formulário FuncionarioForm que criamos no forms.py
        form = FuncionarioForm()
    dados = {
        'form': form,
    }
    return render(request, 'funcionarios/funcionarios_cadastrar.html', dados)


def funcionarios_editar(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except:
        return redirect('funcionarios')

    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios')

    # form vai receber um formulário com os dados do funcionario selecionado.
    form = FuncionarioForm(instance=funcionario)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'funcionario': funcionario,
    }

    return render(request, 'funcionarios/funcionarios_editar.html', dados)


def desativar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
        funcionario.ativo = False  # Desativa o funcionário
        funcionario.save()
        messages.success(request, "Funcionário desativado com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este funcionário, pois ele está vinculado a uma reserva.")
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")

    return redirect('funcionarios')


def ativar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")
        return redirect('funcionarios_inativos')

    if funcionario.ativo == False:
        funcionario.ativo = True
        funcionario.save()
        messages.success(request, "Funcionario reativado com sucesso.")

    else:
        messages.info(request, "O funcionário já está ativo.")

    return redirect('funcionarios_inativos')


def funcionarios_inativos(request):
    funcionarios = Funcionario.objects.filter(ativo=False)
    dados = {
        'funcionarios': funcionarios,
        'ativos': False,
    }
    return render(request, 'funcionarios/index.html', dados)

# IMOVEIS


def imoveis(request):
    imoveis = Imovel.objects.filter(ativo=True)

    dados = {
        'imoveis': imoveis,
        'ativos': True,  # Para indicar que estamos mostrando imóveis ativos
    }

    return render(request, 'imoveis/index.html', dados)


def imoveis_cadastrar(request):
    if request.method == 'POST':
        form = ImovelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('imoveis')
    else:
        form = ImovelForm()  # form vai receber um formulário ImovelForm que criamos no forms.py
    dados = {
        'form': form,
    }
    return render(request, 'imoveis/imoveis_cadastrar.html', dados)


def imoveis_editar(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
    except:
        return redirect('imoveis')

    if request.method == 'POST':
        form = ImovelForm(request.POST, instance=imovel)
        if form.is_valid():
            form.save()
            return redirect('imoveis')

    # form vai receber um formulário com os dados do imoveis selecionado.
    form = ImovelForm(instance=imovel)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'imovel': imovel,
    }

    return render(request, 'imoveis/imoveis_editar.html', dados)


def desativar_imovel(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
        imovel.ativo = False  # Desativa o imóvel
        imovel.save()
        messages.success(request, "Imóvel desativar com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este imóvel, pois ele está vinculado a uma reserva.")
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")

    return redirect('imoveis')


def ativar_imovel(request, id):
    try:
        imovel = Imovel.objects.get(id=id)
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")
        return redirect('imoveis_inativos')

    if imovel.ativo == False:
        imovel.ativo = True
        imovel.save()
        messages.success(request, "Imóvel reativado com sucesso.")

    else:
        messages.info(request, "O imóvel já está ativo.")

    return redirect('imoveis_inativos')


def imoveis_inativos(request):
    imoveis = Imovel.objects.filter(ativo=False)
    dados = {
        'imoveis': imoveis,
        'ativos': False,
    }
    return render(request, 'imoveis/index.html', dados)

# CLIENTES


def clientes(request):
    clientes = Cliente.objects.filter(ativo=True)

    dados = {
        'clientes': clientes,
        'ativos': True,  # Para indicar que estamos mostrando clientes ativos
    }

    return render(request, 'clientes/index.html', dados)


def clientes_cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()  # form vai receber um formulário ClienteForm que criamos no forms.py
    dados = {
        'form': form,
    }
    return render(request, 'clientes/clientes_cadastrar.html', dados)


def clientes_editar(request, id):

    try:
        cliente = Cliente.objects.get(id=id)
    except:
        return redirect('clientes')

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes')

    # form vai receber um formulário com os dados do cliente selecionado.
    form = ClienteForm(instance=cliente)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'cliente': cliente,
    }

    return render(request, 'clientes/clientes_editar.html', dados)


def desativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.ativo = False  # Desativa o cliente
        cliente.save()
        messages.success(request, "Cliente desativado com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este cliente, pois ele está vinculado a uma reserva.")
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
    return redirect('clientes')


def ativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect('clientes_inativos')

    if cliente.ativo == False:
        cliente.ativo = True
        cliente.save()
        messages.success(request, "Cliente reativado com sucesso.")

    else:
        messages.info(request, "O cliente já está ativo.")

    return redirect('clientes_inativos')


def clientes_inativos(request):
    clientes = Cliente.objects.filter(ativo=False)
    dados = {
        'clientes': clientes,
        'ativos': False,
    }
    return render(request, 'clientes/index.html', dados)
# RESERVAS


def reservas(request):
    reservas = Reserva.objects.filter(ativo=True)

    dados = {
        'reservas': reservas,
        'ativos': True,  # Para indicar que estamos mostrando reservas ativas
    }

    return render(request, 'reservas/index.html', dados)


def reservas_cadastrar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()  # form vai receber um formulário ReservaForm que criamos no forms.py
    dados = {
        'form': form,
    }
    return render(request, 'reservas/reservas_cadastrar.html', dados)


def reservas_editar(request, id):

    try:
        reserva = Reserva.objects.get(id=id)
    except:
        return redirect('reservas')

    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            form.save()
            return redirect('alunos')

    # form vai receber um formulário com os dados da reserva selecionada.
    form = ReservaForm(instance=reserva)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'reserva': reserva,
    }

    return render(request, 'reservas/reserva_editar.html', dados)


def desativar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
        reserva.ativo = False  # Desativa a reserva
        reserva.save()
        messages.success(request, "Reserva desativada com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar esta reserva, pois ela está vinculada a um imóvel ou cliente.")
    except Reserva.DoesNotExist:
        messages.error(request, "Reserva não encontrada.")
    return redirect('reservas')


def ativar_reserva(request, id):
    try:
        reserva = Reserva.objects.get(id=id)
    except Reserva.DoesNotExist:
        messages.error(request, "Reserva não encontrada.")
        return redirect('reservas_inativas')

    if reserva.ativo == False:
        reserva.ativo = True
        reserva.save()
        messages.success(request, "Reserva reativada com sucesso.")

    else:
        messages.info(request, "A reserva já está ativa.")

    return redirect('reservas_inativas')


def reservas_inativas(request):
    reservas = Reserva.objects.filter(ativo=False)
    dados = {
        'reservas': reservas,
        'ativos': False,
    }
    return render(request, 'reservas/index.html', dados)
