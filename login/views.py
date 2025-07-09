from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        verificacao_user = authenticate(
            request, username=username, password=password)

        if verificacao_user is not None:
            login(request, verificacao_user)
            return redirect('core:index')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'login/login.html')


def logout_view(request):
    logout(request)
    return redirect('auth:login')
