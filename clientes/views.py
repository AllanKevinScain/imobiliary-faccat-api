from django.shortcuts import render
from .models import Cliente
from .forms import ClienteForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError
from django.contrib.auth.decorators import login_required

# CLIENTES
ORDENACAO_CLIENTES_LOOKUP = {
    'nome': 'nome',
    'data_nascimento': 'data_nascimento',
}


@login_required
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


@login_required
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


@login_required
def clientes_cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente cadastrado com sucesso.")
            return redirect('clientes:lista', campo="nome")
    form = ClienteForm()
    dados = {'form': form}
    return render(request, 'clientes/cadastrar.html', dados)


@login_required
def editar_clientes(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except:
        messages.error(request, "Cliente não encontrado.")
        return redirect('clientes:lista', campo="nome")
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Informações atualizadas com sucesso.")
            return redirect('clientes:lista', campo="nome")
    form = ClienteForm(instance=cliente)
    dados = {'form': form, 'cliente': cliente}
    return render(request, 'clientes/editar.html', dados)


@login_required
def desativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
        cliente.ativo = False
        cliente.save()
        messages.success(request, "Cliente "+cliente.nome+" foi desativado.")
    except RestrictedError:
        messages.error(
            request, "Não é possível desativar este cliente, pois ele está vinculado a uma reserva.")
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
    return redirect('clientes:lista_inativos', campo="nome")


@login_required
def ativar_cliente(request, id):
    try:
        cliente = Cliente.objects.get(id=id)
    except Cliente.DoesNotExist:
        messages.error(request, "Cliente não encontrado.")
        return redirect('clientes:lista', campo="nome")
    if cliente.ativo == False:
        cliente.ativo = True
        cliente.save()
        messages.success(request, "Cliente "+cliente.nome+" foi ativado.")
    else:
        messages.info(request, "O cliente já está ativo.")
    return redirect('clientes:lista', campo="nome")
