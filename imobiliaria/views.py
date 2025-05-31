from django.shortcuts import render
from .models import Funcionario, Cliente, Imovel, Quarto, Reserva

# Create your views here.
def index(request):
    return render(request, 'index.html')

def funcionarios(request):
    funcionarios = Funcionario.objects.all()

    dados = {
        'funcionarios': funcionarios,
    }

    return render(request, 'funcionarios/index.html', dados)

def funcionarios_cadastrar(request):
    return render(request, 'funcionarios/funcionarios_cadastrar.html')

def funcionarios_editar(request):
    return render(request, 'funcionarios/index.html')

def imoveis(request):
    imoveis = Imovel.objects.all()

    dados = {
        'imoveis': imoveis,
    }

    return render(request, 'imoveis/index.html', dados)

def imoveis_cadastrar(request):
    return render(request, 'imoveis/imoveis_cadastrar.html')

def imoveis_editar(request):
    return render(request, 'imoveis/index.html')

def clientes(request):
    clientes = Cliente.objects.all()

    dados = {
        'clientes': clientes,
    }

    return render(request, 'clientes/clientes_cadastrar.html', dados)

def clientes_cadastrar(request):
    return render(request, 'clientes/index.html')

def clientes_editar(request):
    return render(request, 'clientes/index.html')

def reservas(request):
    reservas = Reserva.objects.all()

    dados = {
        'reservas': reservas,
    }

    return render(request, 'reservas/index.html', dados)

def reservas_cadastrar(request):
    return render(request, 'reservas/reservas_cadastrar.html')

def reservas_editar(request):
    return render(request, 'reservas/index.html')