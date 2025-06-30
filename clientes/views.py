from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError

# CLIENTES
ORDENACAO_CLIENTES_LOOKUP = {
    'nome': 'nome',
    'email': 'email',
    'data_nascimento': 'data_nascimento',
}


def clientes(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        clientes = Cliente.objects.filter(ativo=True, nome__icontains=query)
    else:
        clientes = Cliente.objects.filter(ativo=True)
    if campo:
        # Esse 'nome'                                            vv serve para garantir que nunca falte um campo, é um valor padrão
        campo_ordenacao = ORDENACAO_CLIENTES_LOOKUP.get(campo, 'nome')
        clientes = clientes.order_by(campo_ordenacao)

    dados = {'clientes': clientes, 'ativos': True,
             'query': query, 'campo': campo}
    return render(request, 'clientes/lista.html', dados)


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
    return render(request, 'clientes/lista.html', dados)


def clientes_cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista', campo="nome")
    else:
        form = ClienteForm()
    dados = {'form': form}
    return render(request, 'clientes/cadastrar.html', dados)


def editar_clientes(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except:
        return redirect('clientes:lista', campo="nome")
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('clientes:lista', campo="nome")
    form = ClienteForm(instance=cliente)
    dados = {'form': form, 'cliente': cliente}
    return render(request, 'clientes/editar.html', dados)


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
    return redirect('clientes:lista_inativos', campo="nome")


def ativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect('clientes:lista', campo="nome")
    if cliente.ativo == False:
        cliente.ativo = True
        cliente.save()
        messages.success(request, "Cliente reativado com sucesso.")
    else:
        messages.info(request, "O cliente já está ativo.")
    return redirect('clientes:lista', campo="nome")
