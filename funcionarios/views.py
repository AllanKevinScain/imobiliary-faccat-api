from django.shortcuts import render
from .models import Funcionario
from .forms import FuncionarioForm
from django.shortcuts import redirect
from django.contrib import messages
from django.db.models import RestrictedError

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
        # Esse 'nome'                                               vv serve para garantir que nunca falte um campo, é um valor padrão
        campo_ordenacao = ORDENACAO_FUNCIONARIO_LOOKUP.get(campo, 'nome')
        funcionarios = funcionarios.order_by(campo_ordenacao)
    dados = {'funcionarios': funcionarios,
             'ativos': True, 'query': query, 'campo': campo}
    return render(request, 'funcionarios/lista.html', dados)


def funcionarios_inativos(request, campo):
    query = request.GET.get('busca', '')
    if campo == 'nome' and query:
        funcionarios = Funcionario.objects.filter(
            ativo=False, nome__icontains=query)
    else:
        funcionarios = Funcionario.objects.filter(ativo=False)
    if campo:
        # Esse 'nome'                                               vv serve para garantir que nunca falte um campo, é um valor padrão
        campo_ordenacao = ORDENACAO_FUNCIONARIO_LOOKUP.get(campo, 'nome')
        funcionarios = funcionarios.order_by(campo_ordenacao)
    dados = {'funcionarios': funcionarios,
             'ativos': False, 'query': query, 'campo': campo}
    return render(request, 'funcionarios/lista.html', dados)


def cadastrar_funcionarios(request):
    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:lista', campo='nome')
    else:
        form = FuncionarioForm()

    dados = {'form': form}
    return render(request, 'funcionarios/cadastrar.html', dados)


def editar_funcionarios(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except:
        return redirect('funcionarios:lista', campo='nome')
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            return redirect('funcionarios:lista', campo='nome')
    form = FuncionarioForm(instance=funcionario)
    dados = {'form': form, 'funcionario': funcionario}
    return render(request, 'funcionarios/editar.html', dados)


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
    return redirect('funcionarios:lista_inativos', campo='nome')


def ativar_funcionario(request, id):
    try:
        funcionario = Funcionario.objects.get(id=id)
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")
        return redirect('funcionarios:lista', campo='nome')
    if funcionario.ativo == False:
        funcionario.ativo = True
        funcionario.save()
        messages.success(request, "Funcionario reativado com sucesso.")
    else:
        messages.info(request, "O funcionário já está ativo.")
    return redirect('funcionarios:lista', campo='nome')
