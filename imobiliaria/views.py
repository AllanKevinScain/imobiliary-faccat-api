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
    funcionarios = Funcionario.objects.all()

    dados = {
        'funcionarios': funcionarios,
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
        funcionario.delete()
        messages.success(request, "Funcionário excluído com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível excluir este funcionário, pois ele está vinculado a uma reserva.")
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")

    return redirect('funcionarios')

# IMOVEIS


def imoveis(request):
    imoveis = Imovel.objects.all()

    dados = {
        'imoveis': imoveis,
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
        imovel.delete()
        messages.success(request, "Imóvel excluído com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível excluir este imóvel, pois ele está vinculado a uma reserva.")
    except Imovel.DoesNotExist:
        messages.error(request, "Imóvel não encontrado.")

    return redirect('imoveis')


# CLIENTES


def clientes(request):
    clientes = Cliente.objects.all()

    dados = {
        'clientes': clientes,
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
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível excluir este cliente, pois ele está vinculado a uma reserva.")
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
    return redirect('clientes')

# RESERVAS


def reservas(request):
    reservas = Reserva.objects.all()

    dados = {
        'reservas': reservas,
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
        reserva.delete()
        messages.success(request, "Reserva excluída com sucesso.")
    except RestrictedError:
        messages.error(
            request, "Não é possível excluir esta reserva, pois ela está vinculada a um imóvel ou cliente.")
    except Reserva.DoesNotExist:
        messages.error(request, "Reserva não encontrada.")
    return redirect('reservas')
