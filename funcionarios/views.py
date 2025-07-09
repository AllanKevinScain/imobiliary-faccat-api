from django.shortcuts import render
from .models import Funcionario
from .forms import FuncionarioForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

ORDENACAO_FUNCIONARIO_LOOKUP = {
    'nome': 'nome',
}


@login_required
def funcionarios(request, campo):
    if not request.user.is_superuser:
        messages.error(request, "Voce não possui acesso a essa página.")
        return redirect('core:index')

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


@login_required
def funcionarios_inativos(request, campo):
    if not request.user.is_superuser:
        messages.error(request, "Voce não possui acesso a essa página.")
        return redirect('core:index')

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


@login_required
def cadastrar_funcionarios(request):
    if not request.user.is_superuser:
        messages.error(request, "Voce não possui acesso a essa página.")
        return redirect('core:index')

    if request.method == 'POST':
        form = FuncionarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Funcionário cadastrado com sucesso.")
            return redirect('funcionarios:lista', campo='nome')
    form = FuncionarioForm()
    dados = {'form': form}
    return render(request, 'funcionarios/cadastrar.html', dados)


@login_required
def editar_funcionarios(request, id):
    if not request.user.is_superuser:
        messages.error(request, "Voce não possui acesso a essa página.")
        return redirect('core:index')

    try:
        funcionario = Funcionario.objects.get(id=id)
    except:
        messages.error(request, "Funcionário não encontrado.")
        return redirect('funcionarios:lista', campo='nome')
    if request.method == 'POST':
        form = FuncionarioForm(request.POST, instance=funcionario)
        if form.is_valid():
            form.save()
            messages.success(request, "Informações atualizadas com sucesso.")
            return redirect('funcionarios:lista', campo='nome')
    form = FuncionarioForm(instance=funcionario)
    dados = {'form': form, 'funcionario': funcionario}
    return render(request, 'funcionarios/editar.html', dados)


@login_required
def desativar_funcionario(request, id):
    if not request.user.is_superuser:
        messages.error(request, "Voce não possui acesso a essa página.")
        return redirect('core:index')

    try:
        funcionario = Funcionario.objects.get(id=id)
        funcionario.ativo = False
        funcionario.save()
        messages.success(request, "O funcionário " +
                         funcionario.nome+" foi desativado.")
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")
    return redirect('funcionarios:lista_inativos', campo='nome')


@login_required
def ativar_funcionario(request, id):
    if not request.user.is_superuser:
        messages.error(request, "Voce não possui acesso a essa página.")
        return redirect('core:index')

    try:
        funcionario = Funcionario.objects.get(id=id)
    except Funcionario.DoesNotExist:
        messages.error(request, "Funcionário não encontrado.")
        return redirect('funcionarios:lista', campo='nome')
    if funcionario.ativo == False:
        funcionario.ativo = True
        funcionario.save()
        messages.success(request, "O funcionário " +
                         funcionario.nome+" foi ativado.")
    else:
        messages.info(request, "O funcionário já está ativo.")
    return redirect('funcionarios:lista', campo='nome')
