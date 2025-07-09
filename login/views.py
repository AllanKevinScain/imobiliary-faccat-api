from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages
from funcionarios.models import Funcionario


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            try:
                funcionario = Funcionario.objects.get(user=user)
            except Funcionario.DoesNotExist:
                funcionario = None

            if user.is_superuser or (funcionario and funcionario.ativo):
                login(request, user)
                return redirect('core:index')
            else:
                messages.error(
                    request, 'Seu acesso foi desativado. Contate um administrador.')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('auth:login')
