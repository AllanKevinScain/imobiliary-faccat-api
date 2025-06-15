from django.shortcuts import render
from .models import Funcionario, Cliente, Imovel, Quarto, Reserva
from .forms import FuncionarioForm, ClienteForm, ImovelForm, QuartoForm, ReservaForm
from django.shortcuts import redirect

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


def funcionarios_editar(request):
    return render(request, 'funcionarios/index.html')

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


def imoveis_editar(request):
    return render(request, 'imoveis/index.html')

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


def clientes_editar(request):
    return render(request, 'clientes/index.html')

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


def reservas_editar(request):
    return render(request, 'reservas/index.html')
