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
    form = ImovelForm(instance=imoveis)

    # Montamos o dicionário com os dados para ser passado para o template.
    dados = {
        'form': form,
        'imovel': imovel,
    }

    return render(request, 'imoveis/imoveis_editar.html', dados)

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
